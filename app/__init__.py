from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .models import PackageTracking
    from .routes import main
    from .admin import CustomModelView

    app.register_blueprint(main)

    admin = Admin(app, name='Delivery Tracker Admin', template_mode='bootstrap4')
    admin.add_view(CustomModelView(PackageTracking, db.session))

    with app.app_context():
        db.create_all()
        seed_data()

    return app

def seed_data():
    from .models import PackageTracking
    if not PackageTracking.query.first():
        sample = PackageTracking(
            tracking_number="123456789",
            status="In Transit",
            last_location="Lagos Facility",
            eta="2025-06-05"
        )
        db.session.add(sample)
        db.session.commit()
