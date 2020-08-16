from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Error reporting
sentry_sdk.init(
    dsn="https://4c0754bd725e4b8b8768185b5f6bbd54@o429436.ingest.sentry.io/5376027",
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG_VALUE") == "True"

ALLOWED_HOSTS = ["https://bookmarket-app.herokuapp.com/", "127.0.0.1", "localhost"]

INSTALLED_APPS = [
    "jazzmin",
    "bootstrapform",
    "crispy_forms",
    "bookmarket.apps.BookmarketConfig",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig",
    "allauth",
    "dj_pagination",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "storages",
    "django_cleanup.apps.CleanupConfig",
    "postman",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "dj_pagination.middleware.PaginationMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "book_app.urls"


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "postman.context_processors.inbox",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "bookmarket.context_processors.messages",
            ],
            "libraries": {  # Adding this section should work around the issue.
                "staticfiles": "django.templatetags.static",
            },
        },
    },
]
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_DISABLE_USER_EMAILING = True
POSTMAN_NOTIFIER_APP = None

WSGI_APPLICATION = "book_app.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Stockholm"
USE_I18N = True
USE_L10N = True
USE_TZ = True

CONTENT_TYPES = ["image", "video"]  # not used
SUPPORTED_FILE_TYPES = ["jpg", "png", "ico"]
# 10485760 - 10 MB
MAX_UPLOAD_SIZE = 5242880  # 5 MB

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "fields": "id,name,email,gender,about,birthday,first_name,hometown",
}
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "locale": "ru_RU",
    "fields": "id, name, email, age_range",
}
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_FACEBOOK_API_VERSION = "2.10"
SITE_ID = os.environ.get("SITE_ID")

CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_REDIRECT_URL = "app-home"
LOGIN_URL = "login"
LOGOUT_URL = "logout"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
DEFAULT_FROM_EMAL = os.environ.get("DEFAULT_FROM_EMAIL")


# ADMINS = [("Admin-" + str(index), admin)
#          for index, admin in enumerate(os.environ.get("DJANGO_ADMINS").split(","))]

# To be able to test, use "False" on the right hand side.
IMAGE_TESTING = os.environ.get("IMAGE_TESTING") == "True"

if DEBUG == True:
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATIC_URL = "/static/"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
else:
    AWS_S3_REGION_NAME = "eu-west-3"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_SIGNATURE_VERSION = "s3v4"
    AWS_S3_ADDRESSING_STYLE = "virtual"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

""" STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'additional'),
) """

JAZZMIN_SETTINGS = {
    "site_title": "Bookmarket Admin",
    "site_header": "Bookmarket",
    "welcome_sign": "Welcome to the Bookmarket Admin Page",
    "copyright": "Bookmarket",
    "search_model": "auth.User",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Production", "url": "https://bookmarket-app.herokuapp.com"},
        {"name": "Localhost", "url": "http://127.0.0.1:8000/"},
        {
            "name": "Github",
            "url": "https://github.com/deslay1/book_app",
            "new_window": True,
        },
        {"model": "auth.User"},
        {"app": "bookmarket"},
    ],
    "usermenu_links": [{"model": "auth.user"}],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["accounts", "bookmarket"],
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-danger",
    "accent": "accent-danger",
    "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-danger",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
}

django_heroku.settings(locals())
