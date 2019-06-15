from .base import *
import dj_databse_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
        )
    }

DEBUG = False