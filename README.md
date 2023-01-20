# Deployment to Fly.io

## Step 1: Install Fly, sign-up and create your app.

    $ brew install flyctl 
    $ fly auth signup 

make sure credit card details are entered

make sure you are in this directory

    $ fly launch
    Creating app in /Users/fitzbe/Documents/shecodes/code/she-codes-crowdfunding-api-project-bendog-1
    Scanning source code
    Detected a Django app
    ? Choose an app name (leave blank to generate one): 
    automatically selected personal organization: Ben Fitzhardinge
    ? Choose a region for deployment: Sydney, Australia (syd)
    Created app rough-brook-8273 in organization personal
    Admin URL: https://fly.io/apps/rough-brook-8273
    Hostname: rough-brook-8273.fly.dev
    Set secrets on rough-brook-8273: SECRET_KEY
    Wrote config file fly.toml
    ? Would you like to set up a Postgresql database now? No
    ? Would you like to set up an Upstash Redis database now? No
    Your app is ready! Deploy with `flyctl deploy`

## Step 2: Configure fly to use your project code.

update `Dockerfile`
```Dockerfile
...
COPY crowdfunding/ /code/

RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
CMD ["/code/run.sh"]
```

update `.dockerignore`
```ignore
fly.toml
.git/
*.sqlite3
venv/
*.pyc
staticfiles/
```

create `crowdfunding/run.sh`
```bash
#!/usr/bin/env bash
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 crowdfunding.wsgi
```

## Step 3: Update your project to work with fly

update your `requirements.txt`
```
Django==4.1.5
djangorestframework==3.14.0
gunicorn==20.1.0
whitenoise==5.3.0
```

Update your virtual env in include these new packages

    $ pip install -r requirements.txt

update the `settings.py` file
```python
...

import os

...

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-6f5fiv53l$d=%d_0_8&znvd!6&d3rfy-qowzswx^u)i-p_dsm6'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG') != 'False'

ALLOWED_HOSTS = ['rough-brook-8273.fly.dev']

...

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]

...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('DATABASE_DIR', BASE_DIR / 'db.sqlite3'),
    }
}

...

STATIC_ROOT = BASE_DIR / 'staticfiles'

...
```

## Step 4: Setup your database volume and configure your settings

then run

    $ chmod +x run.sh 
    $ fly volumes create -r syd --size 1 dbvol 
            ID: vol_w0enxv3x86wv8okp
          Name: dbvol
           App: rough-brook-8273
        Region: syd
          Zone: 2958
       Size GB: 1
     Encrypted: true
    Created at: 20 Jan 23 04:15 UTC

    $ flyctl secrets set DATABASE_DIR='/dbvol/db.sqlite3'
    $ flyctl secrets set DJANGO_SUPERUSER_USERNAME='admin'
    $ flyctl secrets set DJANGO_SUPERUSER_EMAIL='ben@notmyemail.org'
    $ flyctl secrets set DJANGO_SUPERUSER_PASSWORD='very_secure_password'

## Step 5: Check it works!

    $ fly deploy
    $ fly open

