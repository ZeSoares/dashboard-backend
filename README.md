# Flask and Angular Project Structure

This project is structured to have a backend built with Flask and a frontend built with Angular.

## Backend Structure

### app/

- **__init__.py**: An empty file indicating that this directory should be treated as a Python package.

- **routes/**

  - **__init__.py**: Another empty file signifying that this is a package.

  - **main_routes.py**: File where you can define your main application routes. You can create more route files as your project grows.

### config/

- **__init__.py**: Package initializer.

- **settings.py**: File to store configuration variables.

## Virtual Environment (Optional)

- **venv/**: Directory for creating a virtual environment. It helps manage project dependencies.

## Other Files

- **requirements.txt**: File listing Python packages and their versions required for the project.

- **run.py**: Script to run your Flask application.

# Prepare your environment

pip install -r requirements.txt

python -m pip install "pymongo[srv]==3.11"

