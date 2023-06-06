from flask import Blueprint

disease_details_bp = Blueprint('disease_details', __name__)

from .details import get_disease_details
# from .connection import create_connection
from . import routes


