from flask import render_template
from flask_login import login_required
from app.main import bp


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@bp.route('/achievements')
@login_required
def achievements():
    return render_template('achievements.html', title='Achievements')


@bp.route('/exercises')
@login_required
def exercises():
    return render_template('exercises.html', title='Exercises')


@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')


@bp.route('/activity1')
@login_required
def activity1():
    return render_template('activity1.html', title='Activity 1')

@bp.route('/activity4')
@login_required
def activity4():
    return render_template('activity4.html', title='Activity 4')

@bp.route('/activity6')
@login_required
def activity6():
    return render_template('activity6.html', title='Activity 6')
