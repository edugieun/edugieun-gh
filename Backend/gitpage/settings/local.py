from .base import *
from decouple import config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='1g=jf)-w%)2l-fli6+ezbz*ycvpg3v=8nd+aw(gdkp^vthcjb&')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []