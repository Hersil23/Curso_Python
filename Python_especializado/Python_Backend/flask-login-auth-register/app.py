from flask import Flask, jsonify
from auth import auth_bp, token_required
import database

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix='/auth')