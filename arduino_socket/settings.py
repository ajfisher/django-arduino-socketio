import os, sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
full_path = lambda *parts: os.path.join(PROJECT_ROOT, *parts)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'arduino_socket.db',
    }
}

STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h+bsjw#+8()x)o&ft)g2&v-2#n!z)l$gzq@$ijz)l&8m*g(7u9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'arduino_socket.urls'

TEMPLATE_DIRS = (full_path("templates"))
STATICFILES_DIRS = (full_path("static"),)

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_socketio',
)
