from flask import render_template
from flask_login import login_required
from app.main import bp


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@bp.route('/about')
def about():
    return render_template('about.html')
    
@bp.route('/achievements')
@login_required
def achievements():
    return render_template('achievements.html', title='Achivements')

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