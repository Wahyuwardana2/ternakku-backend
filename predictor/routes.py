from flask import Blueprint, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from predictor.predictor import predict_image
from model.model import model
from disease_details.details import get_disease_details

predictor_bp = Blueprint('predictor', __name__)


# # Load your trained model
# model = load_model("server-ternakku/model/1685253926.h5") 

@predictor_bp.route('/predict', methods=['POST'])
def predict():
    # get img
    file = request.files['image']

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
        'handling_method': handling_method
    }
    return jsonify(response)
