from flask import Flask
from authentication import authentication_bp
from authentication import authenticate_token
from predictor import predictor_bp
from disease_details import disease_details_bp

app = Flask(__name__)

app.register_blueprint(authentication_bp, url_prefix='/authentication')
app.register_blueprint(predictor_bp)
app.register_blueprint(disease_details_bp)

@app.route('/')
@authenticate_token
def hello():
    return "<h1>Success, API ready to use</h1>"

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401

if __name__ == "__main__":
    app.run()

