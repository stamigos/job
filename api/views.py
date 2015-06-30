from flask import request, abort, jsonify
from api import db, app
from api.models import User
from datetime import datetime


@app.route('/api/users', methods=['POST'])
def users_post():
    email = request.form['email']
    password = request.form['password']
    info = request.form['info']
    if email is None or password is None:
        abort(400)
    if User.query.filter_by(email=email).first() is not None:
        abort(400)
    user = User(email=email, info=info)
    user.hash_password(password)
    user.registered_on = datetime.utcnow()
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': 'OK', 'user': user.email, 'pass': password})


@app.route('/api/users/', methods=['GET'])
def filter_users():
    users = User.query.all()
    filter = request.args.get('filter')
    str = request.args.get('str')
    if (filter is None) and (str is None):
        return jsonify({'status': 'OK', 'users': [{'user': user.email} for user in users]})
    if users is None:
        abort(400)
    if filter == 'email':
        users = User.query.filter_by(email=str).all()
        if users is None:
            abort(400)
        return jsonify({'status': 'OK', 'users': [{'user': user.email} for user in users],
                        'filter_type': filter, 'filter_name': str})
    else:
        if filter == 'registered_on':
            users = User.query.filter_by(registered_on=str).all()
            if users is None:
                abort(400)
            return jsonify({'status': 'OK', 'users': [{'user': user.email} for user in users],
                            'filter_type': filter, 'filter_name': str})

    return jsonify({'status': 'OK', 'users': [{'user': user.email} for user in users]})