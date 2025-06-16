# Tutorial 1 


## step by step flow to start a project

#### Create and activate virtual environment 

 
    python -m venv env_name
    .\env_name\Scripts\activate




#### Install Django



    python -m pip install django



#### Create the django project


    django-admin startproject project_name  path


#### Run django server


    python manage.py runserver port               
                  // port is optional

 
 



 ### Create an app

 python manage.py startapp app_name

 <p> 
    This will create a folder with some files in the project folder 
 </p>

### Create a view in app and expose to the project

1. Create a function that return a HTTP resonse in the views file 
2. Create a urls.py in the app folder and create a **urlpatterns** list which contains the path("path",views.fn,name)
3. Add the app config to the settings of the project 
4. now in the project main urls.py include the app urlpatterns 
5. now you can see the http response in the browser