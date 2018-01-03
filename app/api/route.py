from flask import Blueprint, render_template, request, redirect, url_for, flash, Markup, jsonify
from flask_classy import FlaskView, route
from app.api.forms import create_database
from app.api.middlewares import MiddleWares
from app import Application

api = Blueprint('api', __name__, template_folder='templates', static_folder='api/static')


class SiteViews(FlaskView, MiddleWares):
    # Default site blueprint base path.
    route_base = '/api/'

    def __int__(self, app, db, ma, csrf):
        super(MiddleWares).__init__()

    # API index route.
    @route("/", methods=['GET', 'POST'])
    def user_home_view(self):
        form = create_database()
        if form.validate_on_submit():
            # Put up the database on submit.
            try:
                self.db.create_all()
                self.db.session.commit()
                message = Markup('<h3>Successfully created!</h3>')
                flash(message=message)
                return redirect(url_for('api.SiteViews:user_home_view'))
            except Exception as e:
                self.db.session.rollback()
                message = Markup('<h3 style="color:red;">' + str(e) + '</h3>')
                flash(message=message)
                return redirect(url_for('api.SiteViews:user_home_view'))
        return render_template('index.html', create_db_form=form)

    # Task injection method to the database.
    @route('add_task', methods=['POST'])
    @Application.csrf.exempt
    def create_new_task(self):
        data = request.get_json()
        # Add task to the database.
        try:
            return MiddleWares.create_task(self, data)
        except Exception:
            pass

    # Update Existing task
    @route('update_task', methods=['PUT'])
    @Application.csrf.exempt
    def update_existing_task(self):
        data = request.get_json()
        # Call middleware / update data in the database.
        try:
            return MiddleWares.update_task(self, data)
        except Exception as exception:
            return "error" + str(exception)

    # Select only one task
    @route('task/<int:tid>', methods=['GET'])
    @Application.csrf.exempt
    def get_task(self, tid):
        try:
            return MiddleWares.get_existing_task(self, tid)
        except Exception:
            pass

    # Select all the existing task.
    @route('tasks', methods=['GET'])
    @Application.csrf.exempt
    def get_all_tasks(self):
        try:
            return MiddleWares.get_all_existing_task(self)
        except Exception:
            pass

    # Select all the complete task.
    @route('complete_tasks', methods=['GET'])
    @Application.csrf.exempt
    def get_all_complete_tasks(self):
        try:
            return MiddleWares.get_all_completed_task(self)
        except Exception:
            pass

    # Delete task from database.
    @route('del_task/<tid>', methods=['DELETE'])
    @Application.csrf.exempt
    def delete_a_task(self, tid):
        data = int(tid)
        try:
            return MiddleWares.delete_task(self, data)
        except Exception as exception:
            return jsonify({"response": str(exception)})

    # Update Existing task
    @route('complete_task', methods=['PUT'])
    @Application.csrf.exempt
    def update_task(self):
        data = request.get_json()
        # Call middleware / update data in the database.
        try:
            return MiddleWares.complete_existing_task(self, data)
        except Exception as exception:
            return "error" + str(exception)



