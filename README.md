# Django Project

## Project Setup

### Prerequisites
- Python (version 3.7 or higher)
- Django (version 3.x or higher)
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the Repository**:
    ```bash
    https://github.com/AntoJebi7/web-app-django.git
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


