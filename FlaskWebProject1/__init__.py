"""
The flask application package.
"""
import os
# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
from flask import Flask
app = Flask(__name__)
app.debug = True
import FlaskWebProject1.views
