from flask import Flask, jsonify
from auth import auth_bp
import database

app = Flask(__name__)

database.init_db()

app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__ == '__main__':
  # Ejecutamos nuestra aplicacion
  app.run(debug=True)