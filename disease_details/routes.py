from flask import Blueprint, jsonify
from . import get_disease_details
from . import disease_details_bp

@disease_details_bp.route('/details/<disease_name>', methods=['GET'])
def details(disease_name):
    disease_details, handling_method = get_disease_details(disease_name)

    response = {
        'disease_name': disease_name,
        'disease_details': disease_details,
        'handling_method': handling_method
    }

    return jsonify(response)
