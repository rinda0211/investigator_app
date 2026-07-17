from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from investigator_app import app

app = Flask(__name__)
app.config.from_object('investigator_app.config')

db = SQLAlchemy(app)
from .models import investigator

import investigator_app.views

if __name__ == '__main__':
    app.run()