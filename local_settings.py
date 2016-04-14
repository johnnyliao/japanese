
DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "japanese",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}

"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "japanese",
        "USER": "root",
        "PASSWORD": "liao12345",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
"""

# Make this unique, and don't share it with anybody.
SECRET_KEY = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

#################
# email setting #
#################

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''

###############
# GEO setting #
###############

GEOS_LIBRARY_PATH = 'C:/OSGeo4W/bin/geos_c.dll'
