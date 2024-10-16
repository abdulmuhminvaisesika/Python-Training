# 16-10-2024
# Django introduction and installation 


## 1. Introduction to Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. It follows the model-template-views (MTV) architectural pattern and is known for its simplicity and reusability. Django is designed to help developers focus on writing apps without needing to reinvent the wheel for common tasks like authentication, database management, and URL routing.

### Key Features of Django:
* Scalability: Django is designed for rapid development but can also scale for large-scale applications.
* Security: It provides built-in protections against security vulnerabilities, such as SQL injection, cross-site scripting, and cross-site request forgery.
* Admin Interface: Django provides an automatically generated admin interface to manage data without additional effort.
* ORM (Object-Relational Mapping): A powerful and intuitive way to interact with databases using Python code instead of writing raw SQL.


### 2. Setting up Django
**Step 1:** Creating a Virtual Environment (venv)
A virtual environment is a self-contained directory that holds a Python installation and necessary libraries. This helps isolate dependencies for your project.

*Commands:*
```
python -m venv my_env
cd my_env\Scripts\activate

```

**Step 2:** Installing Django
Once the virtual environment is activated, you can install Django.

*Command:*
```

pip install django

```
### 3. Creating a Django Project
After installing Django, you can create a new project. A project in Django is the entire application setup that includes settings, configurations, and apps.


*Command:*
```
django-admin startproject myproject

```
This command will create a folder named myproject, which will have the following structure:

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### 4. Creating a Django App
In Django, an app is a component of a project, responsible for handling a specific aspect of the website (e.g., blog, user authentication). You can have multiple apps within a project.


*Command:*
```
python manage.py startapp myapp
```
This will create a directory structure like this:

```
myapp/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```
### 5. Setting Up the Project

After creating the app, you need to add it to the project’s configuration. Open myproject/settings.py and add the name of your app to the INSTALLED_APPS list:


```
INSTALLED_APPS = [
    ...
    'myapp',
]
```
**Running Migrations**
Before starting the server, apply migrations to set up the initial database schema:


```
python manage.py migrate
```
### 6. Running the Server

```
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser, and you should see the Django welcome page.

---
# Django ORM Queries and Model Managers

### 1. Create
**save()**

Creates and saves a new object to the database.

*Syntax:*
```
instance.save()
```

**create()**

Creates a new object and saves it in one step.
**Syntax:*

```
Model.objects.create(field1=value1, field2=value2, ...)
```
### 2. Read (Retrieve)
**all()**

Retrieves all records from the database.

*Syntax:*
```
Model.objects.all()
```
**get()**

Retrieves a single record that matches the given condition. Raises an error if no match or multiple matches are found.

*Syntax:*
```
Model.objects.get(condition)
```
**filter()**

Retrieves all records that match the given condition(s).

*Syntax:*
```
Model.objects.filter(condition)
```
### 3. Update

**save()**

Updates an existing object’s fields and saves the changes to the database.
*Syntax:*
```
instance.save()
```
**update()**

Updates one or more records that match the given condition(s).

*Syntax:*

```
Model.objects.filter(condition).update(field1=value1, ...)
```
### 4.Delete
**delete()**

Deletes an object or a set of objects that match the given condition(s).
*Syntax:*
```
instance.delete()  # Single object
Model.objects.filter(condition).delete()  # Multiple objects
```
### 5.Other methods


**exclude()**
Excludes records that match the given condition(s).

*Syntax:*
```
Model.objects.exclude(condition)
```
**order_by()**
Orders the QuerySet by the specified field(s). Use a hyphen (-) for descending order.
*Syntax:*
``` python
Model.objects.order_by('field')        # Ascending order
Model.objects.order_by('-field')       # Descending order
```
**count()**
Returns the total number of records in the QuerySet.
*Syntax:*
```
Model.objects.count()
```
**exists()**

Returns True if the QuerySet contains any records, otherwise False.
*Syntax:*
```
Model.objects.filter(condition).exists()
```
**first()**

Returns the first object in the QuerySet or None if no records are found.
*Syntax:*
```
Model.objects.first()
```
**last()**

Returns the last object in the QuerySet or None if no records are found.
*Syntax:*
```
Model.objects.last()
```


---