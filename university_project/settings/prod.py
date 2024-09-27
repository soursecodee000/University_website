import dj_database_url
from .common import *
import os

SECRET_KEY=os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['uni-prod-31552cb0c12e.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}



## email sending app
EMAIL_HOST=os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER=os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD=os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT=os.environ['MAILGUN_SMTP_PORT']