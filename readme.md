install python  
install pip  
install django (Check the docs)  
install postgres  
run the following on cmd  
* pip install django-user-sessions  
* pip install django-cors-headers  
* pip install couchdb  
* pip install django-guardian  
* pip install djangorestframework  

cd into rentright/rentright directory  
run  python manage.py migrate    
run python manage.py createsuperuser  
enter an admin username and password
run python manage.py runserver  
to access the admin go to localhost:8000/admin on your browser  




 Check Settings.py and edit  
 DATABASES = {  
   'default': {  
       'ENGINE': 'django.db.backends.postgresql',  
       'NAME': 'postgres',//.......name of your postgres database instance  
        'USER' :'postgres','PASSWORD':'password' // ..........username of ur instance  // password of your instance  
   }  
 }  


