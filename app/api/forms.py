# Imports
from flask_wtf import FlaskForm
from wtforms import *


# Create database and all the required tables.
class create_database(FlaskForm):
    create = SubmitField('')
