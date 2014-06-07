from settings import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

def env(setting, default=None):
    """
    Gets the environment setting or raise exception.
    """
    try:
        if default is not None:
            return os.environ.get(setting, default)
        else:
            return os.environ[setting]
    except KeyError:
        error_msg = "Environment variable %s not set" % setting
        raise ImproperlyConfigured(error_msg)


DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : env('DATABASES_DEFAULT_NAME', 'viviendas'),
        'USER' : env('DATABASES_DEFAULT_USER', 'viviendas'),
        'PASSWORD' : env('DATABASES_DEFAULT_PASSWORD','viviendas'),
        'HOST' : env('DATABASES_DEFAULT_HOST', 'localhost'),
        'PORT' : env('DATABASES_DEFAULT_PORT', '5433'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$vk(v3r#-)b52ch)afd0q-9$a^j9$n#w=i!ahr*g7q2ub&qmlw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True