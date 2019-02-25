import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'k82S*P41KUIQfyKb'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    RECAPTCHA_PUBLIC_KEY = "6LdAkpMUAAAAAHd_N2lqr2xausLbKXPp5zsZ-Zq_"
    RECAPTCHA_PRIVATE_KEY = "6LdAkpMUAAAAAPBBuNn0C67W44zizgSidd415PhO"
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
