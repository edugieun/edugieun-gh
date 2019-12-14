from .base import *
from decouple import config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

<<<<<<< HEAD
ALLOWED_HOSTS = ['edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com']
=======
ALLOWED_HOSTS = []

#comment
>>>>>>> 096d9d5dfcb528a2ba7610880fe1695363de87e3
