from app.api import bp
from flask import jsonify
from app.models import User
from flask import request
from flask import url_for
from app import db
from app.api.errors import bad_request
from flask import g, abort
from app.api.auth import token_auth


def test_test_exercises(client):
    response = client.get('/exercises', follow_redirects=True)
    assert response.status_code == 200


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def test_get_user(client, id):
    response = client.get('/users/0', follow_redirects=True)
    assert response.status_code == 200
    # return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
@token_auth.login_required
def test_get_users(client):
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    # return jsonify(data)
    response = client.get('/users', follow_redirects=True)
    assert response.status_code == 200


@bp.route('/users/<int:id>/achievements', methods=['GET'])
@token_auth.login_required
def test_get_achievements(client, id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.achievements, page, per_page,
                                   'api.get_achievements', id=id)
    # return jsonify(data)
    response = client.get('/users/0/achievements', follow_redirects=True)
    assert response.status_code == 200


@bp.route('/users', methods=['POST'])
def test_create_user(client):
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first(client):
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first(client):
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    # return response
    response = client.post('/users', follow_redirects=True)
    assert response.status_code == 200


@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def test_update_user(client, id):
    if g.current_user.id != id:
        abort(403)
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first(client):
        return bad_request('please use a different username')
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first(client):
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())
    response = client.put('/users/0', follow_redirects=True)
    assert response.status_code == 200
