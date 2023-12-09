from flask import Blueprint

customer_routes = Blueprint('customer_routes', __name__)

from .customer_routes import customer_routes
