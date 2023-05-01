import datetime
from . import db


class Urls(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    short = db.Column(db.String(255))
    visits = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=False), default=datetime.datetime.utcnow)

    def __init__(self, original_url, short=None):
        self.original_url = original_url
        self.short = short
