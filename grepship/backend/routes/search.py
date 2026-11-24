from flask import Blueprint, jsonify
from extension import mongo

ser_bp = Blueprint("search", __name__, url_previx="/api/search")
