from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#ef#r0w2z82h)6!uz76n5ai5ujw5e0rdy2%+x&qzp$c^x*v781"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local_app
    "account.apps.AccountConfig",
    "config.apps.ConfigConfig",
    "ticket.apps.TicketConfig",
    "category.apps.CategoryConfig",
    "blog.apps.BlogConfig",
    "job.apps.JobConfig",
    "advertise.apps.AdvertiseConfig",
    "shop.apps.ShopConfig",
    "product.apps.ProductConfig",
    "cart.apps.CartConfig",
    "order.apps.OrderConfig",
    # third_app
    "rest_framework_simplejwt.token_blacklist",
    "debug_toolbar",
    "corsheaders",
    "ckeditor",
    "rest_framework",
    "drf_yasg",
    "storages",
    "rest_framework_simplejwt",
    "comment",
    "jalali_date",
    "azbankgateways",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # third
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "plastapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "plastapp.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "root",
        "PASSWORD": "msZJBaE2XypCD62uDzfcUPTo",
        "HOST": "may.iran.liara.ir",
        "PORT": "30734",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = "fa-ir"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = [
    "127.0.0.1",
]

CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:3000",
#     "http://localhost:3000",
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
#     "http://localhost:3000/",
#     "http://localhost:3030/",
#     "http://localhost:3030",
# ]

AUTH_USER_MODEL = "account.User"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
    },
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

EXPIRY_TIME_OTP = 120

PROFILE_APP_NAME = "account"
PROFILE_MODEL_NAME = "User"
# the field names below must be similar to your profile model fields
COMMENT_PROFILE_API_FIELDS = ("phone_number",)
USERNAME_FIELD = "phone_number"
EMAIL_FIELD = "phone_number"
COMMENT_USER_API_FIELDS = [
    "id",
    "phone_number",
]
COMMENT_PROFILE_API_FIELDS = ("display_name", "birth_date", "image")


AZ_IRANIAN_BANK_GATEWAYS = {
    "GATEWAYS": {
        "MELLAT": {
            "TERMINAL_CODE": "3621439",
            "USERNAME": "p338",
            "PASSWORD": "7193830",
        },
    },
    "IS_SAMPLE_FORM_ENABLE": True,  # اختیاری و پیش فرض غیر فعال است
    "DEFAULT": "MELLAT",
    "CURRENCY": "IRR",  # اختیاری
    "TRACKING_CODE_QUERY_PARAM": "tc",  # اختیاری
    "TRACKING_CODE_LENGTH": 16,  # اختیاری
    "SETTING_VALUE_READER_CLASS": "azbankgateways.readers.DefaultReader",  # اختیاری
    "BANK_PRIORITIES": [
        "MELLAT",
        # and so on ...
    ],  # اختیاری
}
