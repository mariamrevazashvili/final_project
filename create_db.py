from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()
    admin = User(username="admin", password=generate_password_hash("admin123"), is_admin=True)
    db.session.add(admin)
    db.session.commit()

print("Database created and admin user added successfully.")
