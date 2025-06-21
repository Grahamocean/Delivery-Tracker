from app import db

class PackageTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(64), nullable=False, unique=True)
    status = db.Column(db.String(64), nullable=False)
    last_location = db.Column(db.String(128))
    eta = db.Column(db.String(64))

    def __repr__(self):
        return f'<PackageTracking {self.tracking_number}>'
