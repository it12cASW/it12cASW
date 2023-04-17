from pathlib import Path
#importar User de polls
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d2**29b%qn3w52-l1*u0a&r&5)!xna#vtuq4rz#!@3$h9tt9vf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition -> cuando ejecuto migrate creo las tablas para estas apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps nuestras ( polls )
    'polls.apps.PollsConfig',
    'corsheaders',

    'django.contrib.sites', # must
    'allauth', # must
    'allauth.account', # must
    'allauth.socialaccount', # must
    'allauth.socialaccount.providers.google', # new
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '812040518166-trifui9v2mc6nnhgkbud5hn4kj5g6c4s.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = '/login/auth'
LOGIN_REDIRECT_URL = '/login/auth'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # nuestras
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['polls/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    "https://domain.com",
    "https://api.domain.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
    "http://localhost:3000",
    "https://it12casw-backend.fly.dev"
]


SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Decir que la clase usuario es mia, para hacer la autenticacion en mi BD
#AUTH_USER_MODEL = User


# Rutas imagenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Amazon Web Services bucket
#instalar packages:
    #pip install boto3
    #pip install django-storages
#Las access_key son temporales
AWS_ACCES_KEY_ID = 'ASIA42HGDBSN6EKMZ2U6'
AWS_SECRET_ACCESS_KEY = 'iBmGr56IZ5uXfXfOnmF2NooQqrwEn0a7npZgdv8x'
AWS_STORAGE_BUCKET_NAME = 'aswproject'
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEOX//////////wEaDJoMhyrZqxnrgVWIeCLSAYullgAvLfiuIyMT4alUlw5z0x57zBkzfAQWxUH1/kEDO//ZQxod36VoJBJC1YC0dj/eI2L1IJG5Lib1E6Jb6F34ja0qh9EBH/KpNhAPyUngVA7m6lCqjWpXzezmIFhTdckkw1wdey/FqxjaOaddw2JtLciJ1kpt2+A0fNt+GKwUAhj7bGJQ4HR2BVx+BSZAeXutFnKDifWdizdVFihijpSQJTpeAALuVCDIjdN1RFIfOsp53pWdecNE5oKHa6AEAJ5tcmXheLA28AD4zj2EgE7aUCiurtqhBjItO5HeXxGZ5Yb3LsY6KrEzyIBuw9/FLRMtTSCjnnh/TdWQ1W6evspAOxUyO88j'
CSRF_TRUSTED_ORIGINS = ['https://*.fly.dev',]