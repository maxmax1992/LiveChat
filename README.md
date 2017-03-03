# Live Chat

### Introduction
This livechat program is using Django framework for backend implementation 
and Javascript for front end. The backend uses 'channels' library that brings real time to Django project.
See deployed version on [heroku](djlivechat.herokuapp.com).
 
### Installing and running locally:
[1] __Create python virtualenviroment (3.5.2)__  
[2] __activate the enviroment__  
[3] __execute this command in root folder:__  
  
```
pip install -r requirements.txt
```
  
####Now after python libraries are installed: 
  
[4] __make db__  
```
python manage.py makemigrations
```
[5] __migrate db__  
```
python manage.py migrate
```
If you dont have redis installed locally, install it.  
__Open new terminal window and execute follwing command:__  
  
[6] __Execute redis server locally (It's requirement for the channels library to work)__  
```
python manage.py redis-server
```
 In project root:  
[7] __Run the server__    
```
python manage.py runserver
```
[8] __Navigate in your browser to__   
```
localhost:/8000
```

 