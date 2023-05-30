from flask import Flask
from predictor.routes import predictor_bp
from disease_details.routes import disease_details_bp

app = Flask(__name__)

app.register_blueprint(predictor_bp)
app.register_blueprint(disease_details_bp)

@app.route('/')
def hello():
    return "Sucess, ready to use"


if __name__ == '__main__':
    app.run()
