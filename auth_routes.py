from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import mongo

auth_bp = Blueprint("auth", __name__)


# 🔐 REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    users = mongo.db.users

    # Check existing
    if users.find_one({"email": email}):
        return {"message": "User already exists"}, 400

    hashed_password = generate_password_hash(password)

    users.insert_one({
        "name": name,
        "email": email,
        "password": hashed_password
    })

    return {"message": "User registered successfully"}


# 🔐 LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    users = mongo.db.users
    user = users.find_one({"email": email})

    if user and check_password_hash(user["password"], password):
        token = create_access_token(identity=str(user["_id"]))
        return {
            "message": "Login successful",
            "token": token
        }

    return {"message": "Invalid credentials"}, 401