from flask import render_template, jsonify, request, flash
from app import db
from flask_login import login_required, current_user
from app.main import bp
import json
import requests

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home', user=current_user)


@bp.route('/achievements')
@login_required
def achievements():
    return render_template('achievements.html', title='Achievements', user=current_user)


@bp.route('/exercises')
@login_required
def exercises():
    return render_template('exercises.html', title='Exercises', user=current_user)


@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', user = current_user)


@bp.route('/activity1')
@login_required
def activity1():
    return render_template('activity1.html', title='Activity 1', user=current_user, points = current_user.points)

@bp.route('/update_points', methods=['POST'])
@login_required
def update_points():
    user = current_user
    points = (user.points + 20)
    user.points = points
    db.session.add(user)
    db.session.commit()

    return render_template('activity1.html', title='Activity 1', user=current_user, points = points)

@bp.route('/activity4')
@login_required
def activity4():
    return render_template('activity4.html', title='Activity 4',user=current_user, points = current_user.points)

@bp.route('/activity6')
@login_required
def activity6():
    return render_template('activity6.html', title='Activity 6',user=current_user, points = current_user.points)

@bp.route('/activity101')
@login_required
def activity101():
    return render_template('activity101.html', title='Activity 1',user=current_user, points = current_user.points)

@bp.route('/activity2')
@login_required
def activity2():
    return render_template('activity2.html', title='Activity 2',user=current_user, points = current_user.points)

@bp.route('/activity2_classical')
@login_required
def activity2_classical():
    return render_template('activity2_classical.html', title='Classical Music',user=current_user, points = current_user.points)

@bp.route('/activity2_stringed')
@login_required
def activity2_stringed():
    return render_template('activity2_stringed.html', title='String Music',user=current_user, points = current_user.points)

@bp.route('/activity2_piano')
@login_required
def activity2_piano():
    return render_template('activity2_piano.html', title='Music: Piano',user=current_user, points = current_user.points)

@bp.route('/activity2_wind')
@login_required
def activity2_wind():
    return render_template('activity2_wind.html', title='Wind Music',user=current_user, points = current_user.points)

@bp.route('/activity2_natural')
@login_required
def activity2_natural():
    return render_template('activity2_natural.html', title='Natural Sound',user=current_user, points = current_user.points)

@bp.route('/activity2_popular')
@login_required
def activity2_popular():
    return render_template('activity2_popular.html', title='Popular Music',user=current_user, points = current_user.points)

@bp.route('/activity5')
@login_required
def activity5():
    return render_template('activity5.html', title='Activity 5',user=current_user, points = current_user.points)

@bp.route('/contact')
@login_required
def contact():
    return render_template('contact.html', title='Contact Us',user=current_user, points = current_user.points)
