import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    #AWS S3 bucket settings
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_BUCKET = os.getenv('S3Bucketname')

    # google cloud storage settings
    GCS_BUCKET = os.getenv('GCS_BUCKET')
    GOOGLE_SERVICE_ACCOUNT_KEY_PATH = '/path/to/service_account_key.json'
    
    # Allowed file Extensions/formats
    S3_ALLOWED_EXTENSIONS = ['jpg', 'png', 'svg', 'webp', 'mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']
    GOOGLE_ALLOWED_EXTENSIONS = ['doc', 'docx', 'csv', 'pdf']