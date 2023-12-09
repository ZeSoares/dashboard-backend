from flask import Flask
from flask_pymongo import PyMongo
import yaml
from urllib.parse import urlparse, urlunparse
from app.routes import customer_routes
from mongoengine import connect

app = Flask(__name__)
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

app.config.update(config)

database_name = 'sample_analytics' 
parsed_uri = urlparse(app.config['MONGO_URI'])
new_uri_parts = (parsed_uri.scheme, parsed_uri.netloc, f'/{database_name}', '', '', '')
app.config['MONGO_URI'] = urlunparse(new_uri_parts)

mongo = PyMongo(app)

connect(db=database_name, host=app.config['MONGO_URI'])

app.register_blueprint(customer_routes)
