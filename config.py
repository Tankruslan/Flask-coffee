import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    COFFEE_MAIL_SUBJECT_PREFIX = '[COFFEE]'
    COFFEE_MAIL_SENDER = 'COFFEE Admin <admin@gmail.com>'
    COFFEE_ADMIN = os.environ.get('COFFEE_ADMIN')

    @staticmethod
    def init_app(app):
        pass


config = {'basic': Config}
