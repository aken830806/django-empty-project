# DEBUG = True

DOMAIN_NAME = ''

ALLOWED_HOSTS = [DOMAIN_NAME, '<other_host>']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '<database_name>',  # Or path to database file if using sqlite3.
        'USER': '<user>',  # Not used with sqlite3.
        'PASSWORD': '<password>',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}
