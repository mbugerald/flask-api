'''
 - All executables permitting the api routes to interact with the models.
 - Middleware for those who are used to php, it can be considered as the controllers.
'''

# Imports
from flask import jsonify
from app.api.models import *
from app import Application
from datetime import datetime
from sqlalchemy import desc


class MiddleWares(Application):
    def __int__(self, app, db, ma, csrf):
        super(Application).__init__()

    # Create new task middleware.
    def create_task(self, data=None):
        # It should be noted that data should be in the form of json.
        if data is None:
            return jsonify({'response': False})
        new_task = Task(title=data['title'], note=data['note'], username=data['username'],
                        start_date=data['start_date'], end_date=data['end_date'],
                        date_added=datetime.today())
        self.db.session.add(new_task)
        self.db.session.commit()

        return jsonify({"response": True})

    # Update task
    def update_task(self, data=None):
        # pid here I am referring to the passed in ID.
        query = Task.query.filter_by(id=data['id']).first()
        # Verify data exist then update if not return message not existing.
        if not query:
            return jsonify({"response": False})
        query.username = data['username'] or query.username
        query.note = data['note'] or query.note
        query.start_date = data['start_date'] or query.start_date
        query.end_date = data['end_date'] or query.end_date
        query.title = data['title'] or query.title
        query.last_update = data['last_update'] or query.last_update
        query.status = query.status
        self.db.session.commit()
        # return result if data exist.
        return jsonify({"response": True})

    # Get Existing task
    def get_existing_task(self, tid=None):
        # Query database for the existing task
        query = Task.query.filter_by(id=tid).first()
        task_schema = TaskSchema(many=False)
        mash_result = task_schema.dump(query).data
        if not query:
            return jsonify({"response": False})
        return jsonify(mash_result)

    # Get all existing task
    def get_all_existing_task(self):
        # Query for all the existing task
        query = Task.query.filter_by(status="available").order_by(desc("id")).all()
        tasks_schema = TaskSchema(many=True)
        mash_result = tasks_schema.dump(query).data
        if not query:
            return jsonify({"response": False})
        return jsonify(mash_result)

    # Get all existing task
    def get_all_completed_task(self):
        # Query for all the existing task
        query = Task.query.filter_by(status="complete").order_by(desc("id")).all()
        tasks_schema = TaskSchema(many=True)
        mash_result = tasks_schema.dump(query).data
        if not query:
            return jsonify({"response": False})
        return jsonify(mash_result)

    # Remove an existing task
    def delete_task(self, task=None):
        # Query for existing task
        if task is None:
            return jsonify({"response": False})
        query = Task.query.filter_by(id=task).first()
        if not query:
            return jsonify({"response": False})
        self.db.session.delete(query)
        self.db.session.commit()
        return jsonify({"response": True})

    # complete an existing task
    def complete_existing_task(self, pid=None):
        # Query for existing result
        query = Task.query.filter_by(status="available", id=pid['id']).first()
        if query is None:
            return jsonify({"response": False})
        query.status = "complete"
        self.db.session.commit()
        # return result if data exist.
        return jsonify({"response": True})
