'''
 - All executables permitting the api middlewares to interact with the database.
'''

# Imports
from app import Application
from datetime import datetime

db = Application().db
ma = Application().ma


# Task object
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(80))
    note = db.Column(db.Text)
    username = db.Column(db.VARCHAR(120))
    start_date = db.Column(db.VARCHAR(120))
    end_date = db.Column(db.VARCHAR(120))
    date_added = db.Column(db.VARCHAR(120), default=datetime.today())
    last_update = db.Column(db.VARCHAR(120))
    status = db.Column(db.VARCHAR(40), default="available")

    def __int__(self, title, note, username, start_date, end_date, date_added, last_update, status):
        self.title = title
        self.note = note
        self.username = username
        self.start_date = start_date
        self.end_date = end_date
        self.date_added = date_added
        self.last_update = last_update
        self.status = status


# Marshmallow for Task
class TaskSchema(ma.Schema):
    class Meta:
        model = Task
        fields = ["id", "title", "username", "note", "start_date", "date_added", "end_date", "last_update", "status"]


