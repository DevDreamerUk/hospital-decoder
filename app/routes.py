from flask import Blueprint, request, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home_page.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')