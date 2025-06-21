from flask import Blueprint, render_template, request, jsonify
from .models import PackageTracking

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
        'eta': package.eta
    })
