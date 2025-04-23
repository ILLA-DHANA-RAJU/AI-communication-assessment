import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'devkey'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
