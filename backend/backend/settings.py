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

    # API rest
    'rest_framework',
    'rest_framework.authtoken', # token authentication

    # AMAZON
    'storages',
]

# Primera opción para el LOCAL
# Segunda opción para el DEPLOY

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '345199254858-e4d431t1ku54g9r99ob4gk93u0788ebn.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '517612110729-ticc5u2mhr5ru2en798ios632bcsaaf7.apps.googleusercontent.com'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# SOCIAL_AUTH_REDIRECT_IS_HTTPS = 'http://127.0.0.1:8000/main/login/auth'
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = 'https://it12casw-backend.fly.dev/login/auth'

# LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/main/login/auth'
LOGIN_REDIRECT_URL = '/login/auth'
#LOGIN_REDIRECT_URL = 'http://it12casw-backend.fly.dev/accounts/google/login/callback/'



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
    "https://editor.swagger.io",
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


# CREDENCIALES AMAZON



AWS_SESSION_TOKEN='FwoGZXIvYXdzEDEaDFbIptMtmkN55Pl1ASLbAZ4PQKbmm/tx4NAuxgDv7JWm2EOOKRanWUgz7gk09/dKscLU9i/3eViXRm1S1jv3dOZdIY0djKGWBhUeLwnT1hinp6nrHTBQ8IgAaL9VWxKOI5CoyJPL4dXym+VOLtXRR4UqO+dsArtSDKR0XVpEeYFUfn2zg6jIGq8VBhQ5cnWYMH3yWFeQ8Sg+DtjS6E8FQrkQ+TID/zbEW9foTBFl68zyRyOiCKnhcDe6GiKBTAQiYXmzzeYpXCof1f8dS3HnSnmOY8XgNkfEA8BPplfX70izYD2SiawjD2Ns2ij485OjBjItqjyJ02xlSShksijCEiC2e3CZ83ggGYdyvySYMGnsaegZ+NVmN/rgepqm+OC8'
AWS_ACCESS_KEY_ID='ASIAUQOHFI6XEJBGFWOY'
AWS_SECRET_ACCESS_KEY='npx4dETY6HQHJu2V/b1OKHYd/fBhpFj7bByWN+OA'



AWS_STORAGE_BUCKET_NAME = 'test-miguel-bucket'
AWS_S3_REGION_NAME='us-east-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = 'public-read'


CSRF_TRUSTED_ORIGINS = ['https://*.fly.dev',]
