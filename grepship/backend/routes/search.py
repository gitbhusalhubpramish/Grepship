from flask import Blueprint, jsonify
from extensions import mongo

ser_bp = Blueprint("search", __name__, url_prefix="/api/search")
