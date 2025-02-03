from app import db, app
from app.models import User


def create_test_users():
    with app.app_context():
        db.create_all()

        admin_user = User.query.filter_by(username="admin").first()
        if not admin_user:
            admin_user = User(
                username="admin",
                email="adminuser@haroncomputer.com",
                role="admin",
            )
            admin_user.set_password("admin123")
            db.session.add(admin_user)

        business_user = User.query.filter_by(username="business").first()
        if not business_user:
            business_user = User(
                username="business",
                email="businessuser@haroncomputer.com",
                role="business",
            )
            business_user.set_password("business123")
            db.session.add(business_user)

        try:
            db.session.commit()
            print("Test users created successfully!")
        except Exception as e:
            print("Error creating users:", str(e))
            db.session.rollback()


if __name__ == "__main__":
    create_test_users()
