from flask import Blueprint, jsonify

#Creo mi blueprint para los productos que tendra un nombre unico y apuntara a el archivo donde fue creado utilizando __name__
users_blueprint = Blueprint('users_bp', __name__)

# Simulated user data
users_db = [
    {"id": 1, "name": "Herasi", "email": "HdPQH@example.com"},
    {"id": 2, "name": "Paula", "email": " VwOy5@example.com"},
    {"id": 3, "name": "Jean", "email":"I0M8M@example.com"},
    {"id": 4, "name": "David", "email": "HtN9o@example.com"},
    {"id": 5, "name": "Eve", "email": "HtN9o@example.com"},
]

@users_blueprint.route("/")
def get_users():
    return jsonify(users_db)

#crear un endpoint para obtener un solo usuario

@users_blueprint.route("/<int:user_id>")