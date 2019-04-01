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
    flash('Congratulations, you have earned 20 points!')
    return render_template('activity1.html', title='Activity 1', user=current_user)

@bp.route('/update_points', methods=['POST'])
@login_required
def update_points():
    data = request.get_json()


    user = current_user
    user.points = data['points']
    db.session.add(user)
    db.session.commit()

    return render_template('activity1.html', title='Activity 1', user=current_user)
