from flask import render_template, flash, redirect, request, url_for, Response
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
import time

from app import db
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp
from app.models import User



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/achievements')
def achievements():
    return render_template('achievements.html')
    
@bp.route('/activity1')
def activity1():
    return render_template('activity1.html')

@bp.route('/about')
def about():
    return render_template('about.html')    

@bp.route('/progress')
def progress():
    def generate():
        x = 0

        while x <= 100:
            yield "data:" + str(x) + "\n\n"
            x = x + 2
            time.sleep(0.6)

    return Response(generate(), mimetype='text/event-stream')


@bp.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html')
    else:
        return redirect(url_for('auth.login'))
