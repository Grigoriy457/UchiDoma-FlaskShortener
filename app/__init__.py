from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.Config")


db = SQLAlchemy(app)
db.session.autocommit = True


from . import models, routes


db.create_all()
