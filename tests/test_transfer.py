''' Test Cases for Transfer Module '''
import sys
import os
import unittest
from unittest.mock import patch, MagicMock


parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from transfer.transfer import Transfer
# from google.cloud import storage

# Define test directory and allowed extensions for testing
TEST_DIR = os.path.dirname(__file__)  

# Path to current test directory
# IMAGE_EXTENSIONS = ['jpg', 'png', 'svg', 'webp']
# MEDIA_EXTENSIONS = ['mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']
# DOCUMENT_EXTENSIONS = ['doc', 'docx', 'csv', 'pdf']

class TestTransfer(unittest.TestCase):

    @patch('boto3.client')
    def test_transfer_files_s3(self, mock_boto_client):
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        transfer_module = Transfer()
        transfer_module._upload_to_s3 = MagicMock()
        transfer_module._upload_to_gcs = MagicMock()

        transfer_module.transfer_files(os.path.join(TEST_DIR, 'files_to_upload'))
        print('file to upload path : ',os.path.join(TEST_DIR, 'files_to_upload'))

        # self.assertEqual(transfer_module._upload_to_s3.call_count, 2)
        # self.assertEqual(transfer_module._upload_to_gcs.call_count, 0)

    @patch('google.cloud.storage.Client')
    def test_transfer_files_gcs(self, mock_storage_client):
        mock_gcs_client = MagicMock()
        mock_storage_client.return_value = mock_gcs_client

        transfer_module = Transfer()
        transfer_module._upload_to_s3 = MagicMock()
        transfer_module._upload_to_gcs = MagicMock()

        os.path.join(TEST_DIR, 'files_to_upload')

        transfer_module.transfer_files(os.path.join(TEST_DIR, 'files_to_upload'))

    #     self.assertEqual(transfer_module._upload_to_s3.call_count, 0)
    #     self.assertEqual(transfer_module._upload_to_gcs.call_count, 1)

    @patch('boto3.client')
    def test_transfer_files_invalid_extension(self, mock_boto_client):
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        transfer_module = Transfer()
        transfer_module._upload_to_s3 = MagicMock()
        transfer_module._upload_to_gcs = MagicMock()

        transfer_module.transfer_files(os.path.join(TEST_DIR, 'files_to_upload'))

        self.assertEqual(transfer_module._upload_to_s3.call_count, 2)  # jpg
        self.assertEqual(transfer_module._upload_to_gcs.call_count, 2)  # pdf

    @patch('boto3.client')
    def test_transfer_files_no_allowed_extensions(self, mock_boto_client):
        mock_s3_client = MagicMock()
        mock_boto_client.return_value = mock_s3_client

        transfer_module = Transfer()
        transfer_module._upload_to_s3 = MagicMock()
        transfer_module._upload_to_gcs = MagicMock()

        transfer_module.transfer_files(os.path.join(TEST_DIR, 'files_to_upload'))

        self.assertEqual(transfer_module._upload_to_s3.call_count, 2)
        self.assertEqual(transfer_module._upload_to_gcs.call_count, 2)

if __name__ == '__main__':
    unittest.main()