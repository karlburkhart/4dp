from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mm-24*i-6iecm7c@z9l+7%^n4564564535s^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEV_VERSION = True
REDMINE_ID = 15497


ALLOWED_HOSTS = [
        '.p4d.hephaistos.arz.oeaw.ac.at',
        '.p4d.acdh-dev.oeaw.ac.at',
        '.p4d.hephaistos.arz.oeaw.ac.at',
        '.p4d.acdh.oeaw.ac.at',
        '127.0.0.1'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '4DPuzzle',
        'USER': 'fterra',
        'PASSWORD': 'r3sid3nt',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
