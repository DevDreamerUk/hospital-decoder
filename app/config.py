import os

class Config:
    SECRET_KEY = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:admin@localhost:5432/hospital_decoding')
