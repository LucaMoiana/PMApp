import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!s(of@$p(cm=#(8t_pd74@hqsxa&a_l2c2jg2$-w!2!a$lkg$d'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
