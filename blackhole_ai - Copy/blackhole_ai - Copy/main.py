from flask import Flask, render_template
from app.api.routes import api_bp
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)