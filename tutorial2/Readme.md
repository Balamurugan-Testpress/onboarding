# Tutorial 2


### This chapter is based on the Database connectivity using django


In this I used the default sqlite3 as db

1.  mysite/settings.py, set TIME_ZONE
2.  By default, `INSTALLED_APPS` contains the several apps (in settings.py file)
3.  `py manage.py migrate`  This command is used to install the apps that are mentioned in the INSTALLED_APPS


### How to create a model 

- use models from django.db
- inherit this model.Model in the child class which is gonna be the table name
- add fields to the class and assign field using model which is gonnna be the coloum name
- `py manage.py makemigrations poll` to create the model
- `py manage.py sqlmigrate polls 0001`  This will give the sql command that run to create the model
- `py manage.py migrate` to create those models in db

- `py manage.py shell` to open shell with the apps installed 
- `Question.objects.all()`  to get all the objects 


### To Create a admin


- `py manage.py createsuperuser`  to create an admin with username , password and email Id
- after run the server and head to http://127.0.0.1:8000/admin/ and enter the admin credentials
- you can see the admin dashboardS
- In poll/admin.py add the model to `admin.site.register(model_name)`
- now when you see the admin dashboard you can see the model_name and can be modified 