# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h0)aba%nkewho6&j_hoh&yw31tf$4vzvs8++*f!i223j06i_rp'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}

