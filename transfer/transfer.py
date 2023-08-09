''' module for uploading images and media to S3 Bucket and docs to Google Cloud Storage'''

import sys
import os
import boto3
from google.cloud import storage
#from .config import Config

# adds the directory containing config file
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, parent_dir) 
import config

# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)  

class Transfer:
    '''File transfer class has functions for upload img, media to s3 and docs to gcs'''
    def __init__(self):
        self.aws_bucket_name = config.AWS_BUCKET
        self.gcs_bucket_name = config.GCS_BUCKET
        self.__create_s3_gcs_instance()
              


    def __create_s3_gcs_instance(self):

        try:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id = config.AWS_ACCESS_KEY,
                aws_secret_access_key = config.AWS_SECRET_KEY
            )
            
            self.google_client = storage.Client.from_service_account_json(config.GOOGLE_SERVICE_ACCOUNT_KEY_PATH)            

        except Exception as er:
            print('error in creating cloud instance, check your configuration : ', str(er))

    def transfer_files(self, source_directory):
        '''transfers files from local to cloud'''
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                file_extension = file.split('.')[-1].lower()
                file_path = os.path.join(root, file)
                if file_extension in config.S3_ALLOWED_EXTENSIONS:
                    self._upload_to_s3(file_path)

                elif file_extension in config.GOOGLE_ALLOWED_EXTENSIONS:
                    self._upload_to_gcs(file_path)

                else: 

                    try:
                        raise FileFormatError(f'{file_extension} format is not allowed to upload')
                    
                    except FileFormatError as fe:
                        print(str(fr))
                

    def _upload_to_s3(self, file_path):
        """uploads files to s3 bucket"""
        try:        
            self.s3_client.upload_file(file_path, self.aws_bucket_name, os.path.basename(file_path))
            print('Files uploaded to S3 bucket successfully')

        except Exception as er:
            print('error in uploading file to s3 bucket : ', str(er))
 
    def _upload_to_gcs(self, file_path):

        """ uploads files to Google Cloud Storage"""        
        try:
            gcs_bucket = self.google_client.get_bucket(self.gcs_bucket_name)
            blob = gcs_bucket.blob(os.path.basename(file_path))
            blob.upload_from_filename(file_path)
            print('Files uploaded to GCS successfully')

        except Exception as er:
            print('erorr in uploading docs to GCS', str(er)) 
        

