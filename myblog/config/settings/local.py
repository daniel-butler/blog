from .base import *
from .base import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='n$q_0f-kyxn)rfxsxyh&37xhz@9teo(pskud0(8$+le=875q$1'
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
