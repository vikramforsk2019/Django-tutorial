all Coomand
To Create a Django Project execute: 

$ django-admin startproject django_example

$ cd django_example

$ python manage.py startapp post

To create a migration for this model, use the following command. It will create a migration file inside the migration folder.

$ python3 manage.py makemigrations  

This migration file contains the code in which a Migration class is created that contains the name and fields of employee table.
// 0001_initial.py

After creating a migration, migrate it so that it reflects the database permanently. The migrate command is given below.

$ python3 manage.py migrate  

If no app-name is provided, it shows all migrations applied to the project.

python3 manage.py showmigrations  

We can get app-specific migrations by specifying app-name, see the example.

$ python3 manage.py showmigrations myapp  




How to convert htmp page into django page..
https://dev.to/amartyadev/converting-any-html-template-into-a-django-template-25ob

<"link rel="stylesheet" href="assets/css/bootstrap.min.css">
needs to be changed to 
<link rel="stylesheet" href="{% static 'assets/css/bootstrap.min.css' %}">

To ease up the above process, there exists a python package djangify which can be installed by: 
pip install djangify
djangify -d main/templates/

#tree#
pip install django-mptt
#insert data directly into created table
python manage.py shell

from myapp.models import Genre
rock = Genre.objects.create(name="Rock")
blues = Genre.objects.create(name="Blues")
