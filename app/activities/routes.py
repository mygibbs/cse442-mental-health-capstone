from flask import render_template
from flask_login import login_required
from app.activities import bp


@bp.route('/exercises')
@login_required
def exercises():
    return render_template('exercises.html', title='Exercises')


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
