from flask import render_template, jsonify, request, flash
from app import db
from flask_login import login_required, current_user
from app.main import bp
import json
import requests
import time

@bp.route('/')
@bp.route('/index')
@login_required
def index():

    user = current_user
    if user.achievement1 is None:
        user.achievement1 = 0
        user.achievement2 = 0
        user.achievement3 = 0
        user.achievement4 = 0
        user.achievement5 = 0
        user.achievement6 = 0
        user.achievement7 = 0
        user.achievement8 = 0
        user.achievement9 = 0
        user.achievement10 = 0

    db.session.add(user)
    db.session.commit()
    return render_template('index.html', title='Home', user=current_user)


@bp.route('/achievements')
@login_required
def achievements():
    return render_template('achievements.html', title='Achievements', user=current_user)


@bp.route('/update_achievements', methods=['POST'])
@login_required
def update_achievements():
    user = current_user
    if (user.points//1000 + 1) == 2:
        user.achievement1 = 1;
    if (user.points//1000 + 1) == 5:
        user.achievement2 = 1;
    if (user.points//1000 + 1) == 10:
        user.achievement3 = 1;
    if (user.points//1000 + 1) == 15:
        user.achievement4 = 1;
    if (user.points//1000 + 1) == 20:
        user.achievement5 = 1;
    if (user.points//1000 + 1) == 25:
        user.achievement6 = 1;
    if (user.points//1000 + 1) == 30:
        user.achievement7 = 1;
    if (user.points//1000 + 1) == 40:
        user.achievement8 = 1;
    if (user.points//1000 + 1) == 50:
        user.achievement9 = 1;
    if (user.points//1000 + 1) == 100:
        user.achievement10 = 1;
    db.session.commit()
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
    actualPoint = request.form.get('data', type=int)
    points = actualPoint
    user.points = points
    db.session.add(user)
    db.session.commit()

    return render_template('activity1.html', title='Activity 1', user=current_user, points = points)

@bp.route('/update_lastlogin', methods=['POST'])
@login_required
def update_lastlogin():
    user = current_user
    currtime = time.time()
    lastlogin = user.lastlogin
    multiplier = user.multiplier

    if user.lastlogin is None:#first time login setup
        user.lastlogin = currtime
        user.currstreak = 1
        user.multiplier = 1.00
        db.session.add(user)
        db.session.commit()
        return render_template('index.html', title='Home', user=current_user)

    if currtime-lastlogin > 86400 and currtime-lastlogin < 172800:
        #its been more than 24 hours and less than 48 hours since last login, re-up (or reset if sunday)
        localtime = time.localtime()
        if localtime.tm_wday == 6:#reset on Sundays. tm_wday has value in [0,6] where 0 is monday and 6 is sunday
            user.currstreak = 1
            user.multiplier = 1.00
            user.lastlogin = currtime
            db.session.add(user)
            db.session.commit()
            return render_template('index.html', title='Home', user=current_user)

        user.currstreak = user.currstreak+1 #up streak by 1
        user.lastlogin = currtime #set new lastlogin, user needs to sign in again between 24 to 48 hours from this point to maintain streak

        if user.currstreak == 2:
            user.multiplier = 1.10
        if user.currstreak == 3:
            user.multiplier = 1.50
        if user.currstreak == 4:
            user.multiplier = 2.00
        if user.currstreak == 5:
            user.multiplier = 2.50
        if user.currstreak == 6:
            user.multiplier == 2.75
        if user.currstreak == 7:
            user.multiplier = 3.00

        db.session.add(user)
        db.session.commit()
        return render_template('index.html', title='Home', user=current_user)

    elif currtime-lastlogin > 172800:#user didnt maintain streak, reset
        user.currstreak = 1
        user.multiplier = 1.00
        user.lastlogin = currtime#set new lastlogin, user needs to sign in again between 24 to 48 hours from this point to maintain streak
        db.session.add(user)
        db.session.commit()
        return render_template('index.html', title='Home', user=current_user)

    return render_template('index.html', title='Home', user=current_user)

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
