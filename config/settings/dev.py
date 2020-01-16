from pathlib import Path
from .base import *

DEBUG = True
# debug variable in templates is available only if INTERNAL_IPS are set
# to a not empty list
INTERNAL_IPS = ['127.0.0.1', ]

SITE_ID = 1
SECRET_KEY = ""
MEDIA_ROOT = ""
EMAIL_FILE_PATH = ""
EMAIL_BACKEND = ''
