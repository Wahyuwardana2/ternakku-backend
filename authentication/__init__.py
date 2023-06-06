from flask import Blueprint

authentication_bp = Blueprint('authentication', __name__)
from .auth import authenticate_token
from . import routes

