# Live Chat

### Introduction
This livechat program is using Django framework for backend implementation 
and Javascript for front end. The backend uses 'channels' library that brings real time to Django project.
See deployed version on [heroku](djlivechat.herokuapp.com).
 
### Installing and running locally:
[1] Create python virtualenviroment (3.5.2)  
[2] activate the enviroment  
[3] execute this command in root folder:  
  
```
pip install -r requirements.txt
```
  
Now after python libraries are installed:  
  
[4] make db  
```
python manage.py makemigrations
```
[5] migrate db  
```
python manage.py migrate
```
(Optional) If you dont have redis installed locally, install it.  
Open new terminal window and execute follwing command:  
  
[6] Execute redis server locally (It's requirement for the channels library to work)  
```
python manage.py redis-server
```
 In project root:  
[7] Run the server  
```
python manage.py runserver
```
[8] Navigate in your browser to  
```
localhost:/8000
```

 