# from flask import Blueprint, render_template, request, jsonify
# from .models import PackageTracking

# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('track.html')

# @main.route('/track')
# def track():
#     tracking_number = request.args.get('tracking_number')
#     if not tracking_number:
#         return jsonify({'error': 'No tracking number provided'}), 400

#     package = PackageTracking.query.filter_by(tracking_number=tracking_number).first()

#     if not package:
#         return jsonify({'error': 'Tracking number not found'}), 404

#     return jsonify({
#         'tracking_number': package.tracking_number,
#         'status': package.status,
#         'last_location': package.last_location,
#         'eta': package.eta
#     })


from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import PackageTracking
from . import db

# Public tracking blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('track.html')

@main.route('/track')
def track():
    tracking_number = request.args.get('tracking_number')
    if not tracking_number:
        return jsonify({'error': 'No tracking number provided'}), 400

    package = PackageTracking.query.filter_by(tracking_number=tracking_number).first()
    if not package:
        return jsonify({'error': 'Tracking number not found'}), 404

    return jsonify({
        'tracking_number': package.tracking_number,
        'status': package.status,
        'last_location': package.last_location,
        'eta': package.eta.strftime('%Y-%m-%d') if hasattr(package.eta, 'strftime') else package.eta
    })


# Admin dashboard blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def dashboard():
    packages = PackageTracking.query.all()
    return render_template('admin.html', packages=packages)

@admin.route('/add', methods=['POST'])
def add_package():
    tracking_number = request.form.get('tracking_number')
    status = request.form.get('status')
    last_location = request.form.get('last_location')
    eta = request.form.get('eta')

    if tracking_number and status:
        new_package = PackageTracking(
            tracking_number=tracking_number,
            status=status,
            last_location=last_location,
            eta=eta
        )
        db.session.add(new_package)
        db.session.commit()
    return redirect(url_for('admin.dashboard'))

@admin.route('/delete/<int:id>', methods=['POST'])
def delete_package(id):
    package = PackageTracking.query.get_or_404(id)
    db.session.delete(package)
    db.session.commit()
    return redirect(url_for('admin.dashboard'))
