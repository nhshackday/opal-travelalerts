import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='opal-travelalerts',
    version='0.1',
    packages=['travelalerts'],
    include_package_data=True,
    license='LICENSE',  
    description='The travelalerts OPAL Plugin',
    long_description=README,
    url='http://opal.openhealthcare.org.uk/',
    author='',
    author_email='',
)