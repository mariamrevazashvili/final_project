from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("მომხმარებელი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired()])
    submit = SubmitField("შესვლა")

class RegisterForm(FlaskForm):
    username = StringField("მომხმარებელი", validators=[DataRequired(), Length(min=3)])
    password = PasswordField("პაროლი", validators=[DataRequired(), Length(min=6, message="პაროლი უნდა შეიცავდეს მინიმუმ 6 სიმბოლოს")])
    submit = SubmitField("რეგისტრაცია")

class BuildingForm(FlaskForm):
    title = StringField("სათაური", validators=[DataRequired()])
    image = StringField("სურათის ფაილი", validators=[DataRequired()])
    description = TextAreaField("აღწერა", validators=[DataRequired()])
    submit = SubmitField("დამატება")
