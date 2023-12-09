from flask_pymongo import PyMongo
from mongoengine import Document, StringField, DateTimeField, ListField, IntField, BooleanField

class Customers(Document):
    username = StringField()
    name = StringField()
    address = StringField()
    birthdate = DateTimeField()
    email = StringField()
    accounts = ListField(IntField())
    tier_and_details = StringField()
    active = BooleanField(default=True)  
