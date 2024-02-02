from functools import wraps
from flask import render_template, Blueprint, get_flashed_messages, request, session, redirect, url_for, flash
from werkzeug.security import check_password_hash

from db_utils import get_user_data

auth_bp = Blueprint('auth_endpoints', __name__, template_folder='templates')


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect(url_for('auth_endpoints.login'))

    return wrapped_view


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_data = get_user_data(username)

        if user_data:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data['id']
                session['username'] = user_data['username']
                return redirect(url_for('index'))

        flash('Błędna nazwa użytkownika lub hasło')
        return redirect(url_for('auth_endpoints.login'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_endpoints.login'))
