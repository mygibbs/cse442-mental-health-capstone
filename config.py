import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'k82S*P41KUIQfyKb'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    RECAPTCHA_PUBLIC_KEY = "6LdAkpMUAAAAAHd_N2lqr2xausLbKXPp5zsZ-Zq_"
    RECAPTCHA_PRIVATE_KEY = "6LdAkpMUAAAAAPBBuNn0C67W44zizgSidd415PhO"
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['mygibbs@gmail.com']
    TESTING = False
