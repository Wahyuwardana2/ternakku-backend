from flask import Blueprint, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
import datetime
from . import predict_image
from . import predictor_bp
from authentication import authenticate_token
from model import model
from disease_details import get_disease_details
from google.cloud import storage
import jwt, requests


# Dapatkan path ke file kunci akses layanan
key_path = os.path.join(os.getcwd(), 'ternakku-f8ca7fe0906b.json')

# Inisialisasi client Google Cloud Storage dengan menggunakan file kunci
storage_client = storage.Client.from_service_account_json(key_path)

bucket_name = 'ternakku-predict-backend'

@predictor_bp.route('/predict', methods=['POST'])
@authenticate_token
def predict():
    # get image
    file = request.files['image']

    # generate unique image name
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    image_name = f"image_{current_time}.jpeg"
    original_image_path = f"predict-image-tmp/{image_name}"
    # Save the file
    file.save(original_image_path)
    
    # Get the bucket reference
    bucket = storage_client.get_bucket(bucket_name)

    # Create a blob object with the image name
    blob = bucket.blob(original_image_path)

    # Set the file stream position to the beginning
    file.seek(0)

    # Upload the file stream
    blob.upload_from_file(file,content_type='image/jpeg')


    try:
        # load original image for processing
        image = cv2.imread(original_image_path)
        image = cv2.resize(image, (64, 64)) / 255.0

        # predict
        predicted_class = predict_image(model, image)

        # get disease details, storage link, and handling method
        disease_details, handling_method = get_disease_details(predicted_class)
        storage_bucket = f"https://storage.googleapis.com/ternakku-predict-backend/{original_image_path}"

        # response
        response = {
            'disease_name': predicted_class,
            'disease_details': disease_details,
            'handling_method': handling_method,
            'image_name':image_name,
            'original_image': storage_bucket
        }
    except:
        response = {'message': 'Failed to get the prediction'}

    finally:
        # Remove original image file
        if os.path.exists(original_image_path):
            os.remove(original_image_path)

    return jsonify(response)


@predictor_bp.route('/delete', methods=['DELETE'])
def delete():
    
    image_name = request.json.get('image_name')

    image_path = f"predict-image-tmp/{image_name}"

    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(image_path)
        blob.delete()
        
        response = {'message': 'Image deleted successfully'}
    except:
        response = {'message': 'Failed to delete the image'}

    return jsonify(response)
