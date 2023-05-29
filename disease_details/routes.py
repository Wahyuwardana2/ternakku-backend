from flask import Blueprint, jsonify
from disease_details.details import get_disease_details

disease_details_bp = Blueprint('disease_details', __name__)

@disease_details_bp.route('/details/<disease_name>', methods=['GET'])
def details(disease_name):
    disease_details, handling_method = get_disease_details(disease_name)

    response = {
        'predicted_class': disease_name,
        'disease_details': disease_details,
        'handling_method': handling_method
    }

    return jsonify(response)
