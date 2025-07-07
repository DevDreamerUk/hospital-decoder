from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required

from app.models.user import User

bp = Blueprint('main', __name__)

@login_required
@bp.route('/')
def home():
    return render_template('home_page.html')


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        user = User.get_or_none(User.username == username)

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash("Невірне ім’я користувача або пароль", "danger")

    return render_template('login.html')