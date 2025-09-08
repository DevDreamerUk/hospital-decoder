from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required
from sqlalchemy import inspect, desc, asc

from app.constants import EXCLUDE_ERROR_LIST
from app.extensions import db
from app.models.emz_records import EMZRecord
from app.models.user import User

bp = Blueprint('main', __name__)


@login_required
@bp.route('/')
def home():
    doctors = db.session.query(EMZRecord.executor_name).distinct().all()
    doctors = [d[0] for d in doctors if d[0]]

    error_types = db.session.query(EMZRecord.error_comment).filter(
        ~EMZRecord.error_comment.in_(EXCLUDE_ERROR_LIST)).distinct().all()
    error_types = [e[0] for e in error_types if e[0]]

    return render_template('home_page.html', doctors=doctors, error_types=error_types)


@bp.route('/login')
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


@bp.route('/search', methods=['POST'])
def search():
    doctors = db.session.query(EMZRecord.executor_name).distinct().all()
    doctors = [d[0] for d in doctors if d[0]]

    error_types = db.session.query(EMZRecord.error_comment).filter(
        ~EMZRecord.error_comment.in_(EXCLUDE_ERROR_LIST)).distinct().all()
    error_types = [e[0] for e in error_types if e[0]]

    fullname = request.form.get('fullname')
    date_start = request.form.get('date_start')
    date_end = request.form.get('date_end')
    error_type = request.form.get('error_type')
    flag_error = request.form.get('flag_error')
    emz_type = request.form.get('emz_type')

    query = EMZRecord.query
    query = query.filter(~EMZRecord.error_comment.in_(EXCLUDE_ERROR_LIST))
    if flag_error == 'on':
        query = query.filter(EMZRecord.included_in_statistics.ilike(f"%Ні%"))
    if emz_type == 'on':
        query = query.filter(EMZRecord.emz_type.ilike(f"%Взаємодія%"))
    if fullname:
        query = query.filter(EMZRecord.executor_name.ilike(f"%{fullname}%"))
    if date_start:
        query = query.filter(EMZRecord.episode_start >= date_start)
    if date_end:
        query = query.filter(EMZRecord.episode_end <= date_end)
    if error_type:
        query = query.filter(EMZRecord.error_comment.ilike(f"%{error_type}%"))

    results = query.order_by(asc(EMZRecord.executor_name)).all()

    column_names = [c.name for c in EMZRecord.__table__.columns]

    results_dicts = [{c: getattr(r, c) for c in column_names} for r in results]
    return render_template(
        "home_page.html",
        results=results_dicts,
        column_names=column_names,
        doctors=doctors,
        results_count=len(results),
        error_types=error_types
    )
