"""
Django settings for kintai project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# default
#BASE_DIR = Path(__file__).resolve().parent.parent
'''settingsの移動に伴う構成変更'''
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PARENT_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# default
#SECRET_KEY = 'XXXX'
'''シークレットキー格納先'''
#with open(f'{PARENT_DIR}/auth/secret_key.cnf') as f:
#    secret_key = f.read().strip()

#SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
'''開発環境'''
#DEBUG = True

#ALLOWED_HOSTS = []

'''本番環境'''
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'kintaiapp.apps.KintaiappConfig', # 勤怠管理アプリ作成
    'accounts.apps.AccountsConfig', # ログイン用アプリ追加
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

ROOT_URLCONF = 'kintai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'], # テンプレートをルートディレクトリ配置に変更
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

WSGI_APPLICATION = 'kintai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

'''シークレットパラメータ格納先'''
#with open(f'{PARENT_DIR}/auth/name_db.cnf') as f:
#    name_db = f.read().strip()

#with open(f'{PARENT_DIR}/auth/pswd_db.cnf') as f:
#    pswd_db = f.read().strip()

#with open(f'{PARENT_DIR}/auth/user_db.cnf') as f:
#    user_db = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'], # シークレット格納先を参照
        'USER': os.environ['DATABASE_USER'], # シークレット格納先を参照
        'PASSWORD': os.environ['DATABASE_PASSWORD'], # シークレット格納先を参照
        'HOST': 'localhost', # ホスト名作成後載記載
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja' # 言語を日本語に変更

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo' # タイムゾーンを日本時間に変更

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 未ログインユーザーのログインページへのリダイレクト
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'kintaiapp:index'

# Heroku settings
SECRET_KEY = os.environ['SECRET_KEY']

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Static files (CSS, JavaScript, Images)
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# HerokuのConfigを読み込み
django_heroku.settings(locals())