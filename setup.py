from setuptools import setup, find_packages

setup(
    name='transfer',
    version='1.0.0',
    description='A module to transfer files to AWS S3 and Google Cloud Storage',
    author='Rudresh YO',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'google-cloud-storage',
        'python-dotenv'
    ],
)
