# DEBUG = True
DEBUG = False

DOMAIN_NAME = ''

ALLOWED_HOSTS = ['<host_ip>']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '<database_name>',  # Or path to database file if using sqlite3.
        'USER': '<user>',  # Not used with sqlite3.
        'PASSWORD': '<password>',  # Not used with sqlite3.
        'HOST': '<host>',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '<port>',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}
