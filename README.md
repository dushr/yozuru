# Yozuru CMS

## About project:

TODO

## Project content:

```
(yozuru root):
├── README.md
├── api <- all models
├── auth_app <- auth helper
├── blog <- blog app
├── core <- main project app
├── database <- directory for dev. purposes 
├── etc <- installation scripts etc.
├── logs <- logs from django 
├── manage.py 
├── projects <- projects app
├── static 
├── static_pages <- static pages app
└── templates
```

## How to install:

* `git clone` this project

* Install deps and needed packages via `bash etc/basic_install.sh`

* Configure your virtualenv. [Tutorial](http://simononsoftware.com/virtualenv-tutorial-part-2/)

* Install pip packages via `pip install etc/requirements.txt` in your virtualenv

* Change settings in `core/local_settings.py` # TODO

* Setup django: 

```
./manage.py migrate
./manage.py createsuperuser
```

* Run django with gunicorn and supervisor # TODO

* Login to your app via `youraddress/login` and add content. Enjoy!
 
 
## TODO: 
 
- Likes

- Entry views counter // django-visits 

- Add static files && templates

- Add cache

- Add scripts + readme content

- Configure project for production mode