from flask import render_template, Blueprint
from auth import login_required

forms_bp = Blueprint('forms_endpoints', __name__, template_folder='templates')

@forms_bp.route('/add_form')
@login_required
def add_form():
    return render_template('add.html')


@forms_bp.route('/delete_form')
@login_required
def delete_form():
    return render_template('delete.html')