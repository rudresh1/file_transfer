


######  PREREQUISITS ############

            AWS S3 bucket and Credentials

1. Create s3 bucket and AWS_ACCESS_KEY,  AWS_SECRET_KEY
# AWS_ACCESS_KEY and AWS_SECRET_KEY follow bellow link
https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html


            GCS Bucket and Credentials
2. Create GCS Bucket, Create a new service account or select an existing one and get JSON file containing the credentials.





#### Download this installable module locally (path/to/installable/module/directory) ###

###### File drectory Structure ################

transfer/
|-- transfer/
|   |-- __init__.py
|   |-- transfer.py
|   |-- config.py
|-- tests/
|   |-- test_transfer.py
|-- README.md
|-- setup.py


###### INSTALLATION ##############

Active your virtual environment where your project running 
# Create a virtual environment named 'myenv' if not
python -m venv myenv

# Activate the virtual environment
# On Windows
myenv\Scripts\activate
# On macOS and Linux
source myenv/bin/activate

# create new package in your project dir 'file_transfer'
# install module
pip install path/to/installable/module/directory -t path/to/your/newly/created/packege/file_transfer

# Configuring S3 Bucket, GCS Bucket and  File Extensions in 'transfer' module
Goto  >>  file_transfer/transfer/config.py
configure all properties

# to use this module in your project 
from file_transfer.transfer.transfer import Transfer

# Create object of Transfer 
ft = Transfer()

# call 'transfer_file' method and pass directory path as parameter from where images, media and docs are upload to Cloud
ft.transfer_files(r'path\to\local\files\directory\')
