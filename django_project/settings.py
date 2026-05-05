import environ
from pathlib import Path
import os


env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str),
    SECURE_HSTS_SECONDS=(int,0),
    CSRF_COOKIE_SECURE=(bool,False),
    SESSION_COOKIE_SECURE=(bool,False),
    SECURE_SSL_REDIRECT=(bool,False),
    SECURE_HSTS_INCLUDE_SUBDOMAINS=(bool,False),
    SECURE_HSTS_PRELOAD=(bool,False),
    ALLOWED_HOSTS=(list,['127.0.0.1']),
    DJANGO_LOG_LEVEL=(str, 'INFO'),
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
# Compare the string value explicitly
DEBUG = env('DEBUG')

if not DEBUG:

    SECURE_HSTS_SECONDS =env('SECURE_HSTS_SECONDS')
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env('SECURE_HSTS_INCLUDE_SUBDOMAINS')
    SECURE_HSTS_PRELOAD = env('SECURE_HSTS_PRELOAD')
    SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')
    SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE')
    CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# Application definition

INSTALLED_APPS = [
    'user_login',
    'tours.apps.ToursConfig',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL="/"

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

jazzmin_settings = {
    "site_title": "TBT Admin Portal",
    "site_header": "TBT Admin",
    "site_brand": "TBT Admin Portal",
    "welcome_sign": "Welcome to the TBT Admin Portal",
    "changeform_format": "carousel",
    "site_logo_classes": "i",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
    "dark_mode_theme": "darkly",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
