from flask import Blueprint, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
import datetime
from predictor.predictor import predict_image
from model.model import model
from disease_details.details import get_disease_details

predictor_bp = Blueprint('predictor', __name__)

@predictor_bp.route('/predict', methods=['POST'])
def predict():
    # get image
    file = request.files['image']
     # generate unique image name
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    image_name = f"scanned_image_{current_time}.jpg"
    image_path = f"scanned/{image_name}"
    cv2.imwrite(image_path, image)

    # process image 
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (64, 64)) / 255.0


    # predict
    predicted_class = predict_image(model, image)

    # get disease details and handling method
    disease_details, handling_method = get_disease_details(predicted_class)

    # response
    response = {
        'predicted_class': predicted_class,
        'disease_details': disease_details,
        'handling_method': handling_method,
        'scanned_image': image_path
    }
    return jsonify(response)

@predictor_bp.route('/delete', methods=['POST'])
def delete():
    # get image name from request
    image_name = request.json.get('image_name')

    # construct image path
    image_path = f'scanned/{image_name}'

    try:
        # delete the image file
        os.remove(image_path)
        response = {'message': 'Image deleted successfully'}
    except OSError:
        response = {'message': 'Failed to delete the image'}

    return jsonify(response)
