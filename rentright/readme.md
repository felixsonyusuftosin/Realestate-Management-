* install python
* install pip 
* install django (Check the docs)
* install postgres
* Run the following on cmd
* pip install django-user-sessions
* pip install django-cors-headers
* pip install couchdb
* pip install django-guardian
* pip install djangorestframework

* Run  python manage.py migrate
* run python manage.py runserver


*Check Settings.py and edit 
*.........................................................
* DATABASES = {
*    'default': {
*        'ENGINE': 'django.db.backends.postgresql',
*        'NAME': 'postgres',                                      //.......name of your postgres database instance
 *   'USER' :'postgres','PASSWORD':'password'                    // ..........username of ur instance  // password of your instance
 *   }
* }


