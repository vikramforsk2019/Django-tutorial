## Django installation/execute project
> virtual environment’s are Python’s way of separating dependencies between projects.
```
$ sudo apt install python3-venv
$ mkdir my-project-env
$ python3 -m venv my-project-env
$ source my-project-env/bin/activate

$  sudo apt install python-pip
$ pip install -r requirements.txt
$ python manage.py runserver

# all Coomand
A Django Project execute: 

$ django-admin startproject django_example
$ cd django_example
$ python manage.py startapp post
```
> To create a migration for this model, use the following command. It will create a migration file inside the migration folder.

$ python3 manage.py makemigrations  

> This migration file contains the code in which a Migration class is created that contains the name and fields of employee table.
// 0001_initial.py

> After creating a migration, migrate it so that it reflects the database permanently. The migrate command is given below.

$ python3 manage.py migrate  

> If no app-name is provided, it shows all migrations applied to the project.

$ python3 manage.py showmigrations  

> We can get app-specific migrations by specifying app-name, see the example.

$ python3 manage.py showmigrations myapp 
$ python manage.py runserver




* How to convert htmp page into django page..
 https://dev.to/amartyadev/converting-any-html-template-into-a-django-template-25ob
```
<"link rel="stylesheet" href="assets/css/bootstrap.min.css">
changed to 
<link rel="stylesheet" href="{% static 'assets/css/bootstrap.min.css' %}">

* To ease up the above process, there exists a python package djangify which can be installed by: 
$ pip install djangify
$ djangify -d main/templates/
```
* tree
pip install django-mptt

* insert data directly into created table using shell
```
python manage.py shell
from myapp.models import Genre
rock = Genre.objects.create(name="Rock")
blues = Genre.objects.create(name="Blues")

# Directory Structure
```
