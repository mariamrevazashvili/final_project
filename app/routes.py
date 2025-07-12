from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegisterForm, BuildingForm
from .models import User, Building
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    buildings = Building.query.all()
    return render_template('home.html', buildings=buildings)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('წარმატებით შეხვედი!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('არასწორი მონაცემები', 'danger')
    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('მომხმარებელი უკვე არსებობს!', 'danger')
        else:
            hashed_password = generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('რეგისტრაცია წარმატებით შესრულდა!', 'success')
            return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/add_building', methods=['GET', 'POST'])
@login_required
def add_building():
    if not current_user.is_admin:
        flash("ადმინისტრატორის უფლებები სჭირდება")
        return redirect(url_for('main.home'))

    form = BuildingForm()
    if form.validate_on_submit():
        new_building = Building(
            title=form.title.data,
            image=form.image.data,
            description=form.description.data
        )
        db.session.add(new_building)
        db.session.commit()
        flash("ნაგებობა დამატებულია")
        return redirect(url_for('main.home'))
    return render_template('add_building.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("გამოსვლა შესრულდა წარმატებით!", "info")
    return redirect(url_for('main.login'))

@main.route('/edit_building/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_building(id):
    if not current_user.is_admin:
        flash("ადმინზეა გათვლილი ფუნქცია", "danger")
        return redirect(url_for('main.home'))

    building = Building.query.get_or_404(id)
    form = BuildingForm(obj=building)

    if form.validate_on_submit():
        building.title = form.title.data
        building.image = form.image.data
        building.description = form.description.data
        db.session.commit()
        flash("ნაგებობა განახლდა!", "success")
        return redirect(url_for('main.home'))

    return render_template('edit_building.html', form=form, building=building)


@main.route('/delete_building/<int:id>', methods=['POST'])
@login_required
def delete_building(id):
    if not current_user.is_admin:
        flash("შესრულება შესაძლებელია მხოლოდ ადმინისტრატორისთვის", "danger")
        return redirect(url_for('main.home'))

    building = Building.query.get_or_404(id)
    db.session.delete(building)
    db.session.commit()
    flash("ნაგებობა წაიშალა!", "info")
    return redirect(url_for('main.home'))


@main.route('/contact')
def contact():
    return render_template('contact.html')
