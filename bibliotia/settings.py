import os
from pathlib import Path
from django.contrib.messages import constants as messages
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-z)fk=va9*wv6k883z%e7@9(=vkdv-hop^-*=k0#q151_pt1l^$'

DEBUG = False

ALLOWED_HOSTS = ['34.239.115.180', 'localhost', '127.0.0.1', 'bibliotia.online', 'www.bibliotia.online']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'category',
    'accounts',
    'store',
    'cart',
    'orders',
    'admin_honeypot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bibliotia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'bibliotia.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'

# Database
#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'databasebibliotia',
        #'USER': 'admintia',
        #'PASSWORD': 'admintia',
        #'HOST': 'databasebibliotia.cj7bfyyqmycu.us-east-1.rds.amazonaws.com',
        #'PORT': '5432',
    #}
#}

DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))                    
}


# Password validation
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
LANGUAGE_CODE = 'de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bibliotia/static')
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Messages
MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
}

# SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bibliotia1@gmail.com'
EMAIL_HOST_PASSWORD = 'fofc zqme vpjw tgbj'
EMAIL_USE_TLS = True

# S3 Configuration
#AWS_ACCESS_KEY_ID = 'AKIARL23M7EQWA34MZ5T'
#AWS_SECRET_ACCESS_KEY = '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'
#AWS_STORAGE_BUCKET_NAME = 'bucketbibliotia'
#AWS_S3_SIGNATURE_NAME = 's3v4',
#AWS_S3_REGION_NAME = 'us-east-1'
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL =  None
#AWS_S3_VERITY = True
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Configuración CSRF
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True 

# Orígenes permitidos para CSRF
CSRF_TRUSTED_ORIGINS = [
    'http://bibliotia.online',
    'https://bibliotia.online',
]