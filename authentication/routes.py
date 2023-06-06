from . import authentication_bp
from flask import request, jsonify
import firebase_admin
from firebase_admin import credentials, auth
import jwt, requests
from . import authenticate_token

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate('ternakku-firebase-adminsdk-scpfz-dd0e6b7cf6.json')
firebase_admin.initialize_app(cred)
api_key = 'AIzaSyDDL3t9jYa2HPn34gybHguxCwQC7KICMzQ'
url_api = "https://identitytoolkit.googleapis.com/v1"

@authentication_bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    url = f"{url_api}/accounts:signUp?key={api_key}"
    data = {
        'name': name,
        'email': email,
        'password': password,
        'returnSecureToken': True
    }
    response = requests.post(url, json=data)
    if response.ok:
        register_result = response.json()
        user_id = register_result['localId']
        
        # Set the display name for the user
        display_name = request.form.get('name')
        auth.update_user(user_id, display_name=display_name)
        
        return jsonify({'error': False, 'message': 'User Created'}), response.status_code
    else:
        return jsonify({'error': True, 'message': 'Registration failed'}), response.status_code


@authentication_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    url = f"{url_api}/accounts:signInWithPassword?key={api_key}"
    data = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }
    response = requests.post(url, json=data)
    if response.ok:
        login_result = response.json()
        user_id = login_result['localId']
        display_name = auth.get_user(user_id).display_name
        token = jwt.encode({'userId': user_id,'name': display_name}, 'your-secret-key', algorithm='HS256')
        return jsonify({
            'error': False,
            'message': 'success',
            'loginResult': {
                'userId': user_id,
                'Name': display_name,
                'token': token
            }
        }), response.status_code
    else:
        return jsonify({'error': True, 'message': 'Login failed'}), response.status_code


@authentication_bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        # Decode and verify the token
        decoded_token = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
        # Perform logout logic here
        # For example, you can invalidate the token or perform any necessary cleanup
        return jsonify({'message': 'Logout successful'})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 403

@authentication_bp.route('/protected')
@authenticate_token
def protected():
    user = request.user
    return jsonify({'message': 'Protected endpoint', 'user': user})
