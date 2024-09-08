# Django with MYSQL DB for User Authentication and Dynamic Resources

## Project Setup

### Prerequisites
- Python (version 3.7 or higher)
- Django (version 3.x or higher)
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the Repository**:
    ```bash
    https://github.com/AntoJebi7/Django_Essentials_with_MYSQL_DB.git
    ```

2. **Create a Virtual Environment** (Optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    Install Django and other dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a Django Project**:
    If you haven’t already created the Django project:
    ```bash
    django-admin startproject myproject .
    ```

5. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    Access the server at `http://127.0.0.1:8000/`.

### Creating a New Django App

1. **Create an App**:
    ```bash
    python manage.py startapp myapp
    ```

2. **Register the App**:
    Add your app to the `INSTALLED_APPS` in `settings.py`:
    ```python
    INSTALLED_APPS = [
        # Other apps...
        'myapp',
    ]
    ```

3. **Create Initial Migrations**:
    ```bash
    python manage.py makemigrations myapp
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```


# Django User Authentication System

This project demonstrates a user authentication system in Django, including registration and login functionality with password hashing. This README outlines the setup process, database configuration, and important Django commands.

## Table of Contents

1. [Introduction](#introduction)
2. [SQL Database Creation](#sql-database-creation)
3. [Django Setup](#django-setup)
4. [User Registration Process](#user-registration-process)
5. [Login Process](#login-process)
6. [Password Hashing](#password-hashing)
7. [Django Commands for Migration](#django-commands-for-migration)
8. [Important Topics](#important-topics)

## Introduction

This project sets up a Django application that allows users to register and log in. The registration process includes password hashing for security. Successful login redirects users to a designated blog page.

## SQL Database Creation

1. **Install MySQL**:
   - Ensure MySQL Server and MySQL Workbench are installed on your system.

2. **Create a Database**:
   - Open MySQL Workbench and run the following SQL command to create a new database:

     ```sql
     CREATE DATABASE mydatabase;
     ```

3. **Configure Django to Use MySQL**:
   - Update your Django project's `settings.py` file to configure the database settings.

## Django Setup

1. **Install Dependencies**:
   - Install Django and MySQL client library using pip:

     ```bash
     pip install django mysqlclient
     ```

2. **Create a Django Project**:
   - Create a new Django project:

     ```bash
     django-admin startproject myproject
     ```

3. **Create a Django App**:
   - Inside the project directory, create a new Django app:

     ```bash
     python manage.py startapp registration
     ```

## User Registration Process

1. **Define the Model**:
   - In the `registration` app, define the `Registration` model with fields for username, password, etc.

2. **Create a Registration Form**:
   - Create a Django form for user registration in the `registration/forms.py` file.

3. **Implement the Registration View**:
   - Create a view to handle user registration, validate the form, and save user details.

4. **Create a Registration Template**:
   - Design an HTML template for the registration form.

## Login Process

1. **Implement the Login View**:
   - Create a view to handle user login, validate username and password, and handle redirects.

2. **Create a Login Template**:
   - Design an HTML template for the login form.

## Password Hashing

1. **Hash Passwords During Registration**:
   - Use Django’s `make_password` to hash passwords before saving them to the database.

2. **Verify Passwords During Login**:
   - Use Django’s `check_password` to verify user passwords during login.

## Django Commands for Migration

1. **Create Migrations**:
   - Generate migration files for your models:

     ```bash
     python manage.py makemigrations
     ```

2. **Apply Migrations**:
   - Apply the migrations to create database tables:

     ```bash
     python manage.py migrate
     ```

3. **Create a Superuser** (optional):
   - Create a superuser account to access the Django admin interface:

     ```bash
     python manage.py createsuperuser
     ```

## Important Topics

- **Password Hashing**: Ensures passwords are stored securely in the database.
- **User Authentication**: Validates user credentials during login.
- **Django Migrations**: Manage changes to the database schema.

