from flask import request, jsonify
import jwt

# Middleware untuk memverifikasi token JWT pada setiap permintaan yang membutuhkan otentikasi
def authenticate_token(func):
    def wrapper(*args, **kwargs):
        # Extract token from request headers
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        try:
            # Decode and verify the token
            decoded_token = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
            request.user = decoded_token
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 403

        return func(*args, **kwargs)

    return wrapper