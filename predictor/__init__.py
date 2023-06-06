from flask import Blueprint

predictor_bp = Blueprint('predictor', __name__)

from .predictor import predict_image
from . import routes

