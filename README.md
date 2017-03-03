# Live Chat

### Introduction
This livechat program is using Django framework for backend implementation 
and Javascript for front end. The backend uses 'channels' library that brings real time to Django project.
See deployed version on [heroku](djlivechat.herokuapp.com).
 
### Installing and running locally:
Create python virtualenviroment (3.5.2) 
Activate the enviroment
execute this command in root folder:

`pip install -r requirements.txt`

Now after python libraries are installed:

`python manage.py makemigrations`
`python manage.py migrate`
(Optional) If you dont have redis installed locally, install it.
Open new terminal window and execute follwing command:
`python manage.py redis-server`
 In project root:
`python manage.py runserver`
Navigate in your browser to 
    localhost:/8000

 