__author__ = 'amigos'
import requests
from datetime import datetime


def test_register_post(email, password, info):
    r = requests.post('http://127.0.0.1:5000/api/users', data={'email': email, 'password': password, 'info': info})
    return r.content


def test_filter_users(filter, str):
    r = requests.get('http://127.0.0.1:5000/api/users', params={'filter': filter, 'str': str})
    return r.content

if __name__ == '__main__':
    print 'test_register_post:'
    print test_register_post('user3@ex.com', 'python', '0977774651')
    print 'test_filter_users(filter=email):'
    print test_filter_users('email', 'user2@ex.com')
    print 'test_filter_users(filter=registered_on):'
    print test_filter_users('registered_on', datetime(2015, 6, 30, 17, 12, 31, 94702))