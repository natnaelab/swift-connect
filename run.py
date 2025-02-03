from app import app, db
from setup_users import create_test_users

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_test_users()
        app.run(debug=True)
