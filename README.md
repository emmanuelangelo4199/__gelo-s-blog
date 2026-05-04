# Django Blog Project Documentation

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/emmanuelangelo4199/__gelo-s-blog.git
   cd __gelo-s-blog
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to see the project in action!

## Features
- User authentication and registration
- Post creation, reading, updating, and deletion (CRUD)
- Commenting system for blog posts
- User profiles with customizable settings
- Tags for organizing posts
- Responsive design for mobile users

## Project Structure
```
__gelo-s-blog/
├── blog/                 # Blog app
├── users/                # User management app
├── templates/            # HTML templates
├── venv/                 # Virtual environment
├── manage.py             # Django management script
└── requirements.txt      # Python package requirements
```

## Requirements
- Python 3.6+
- Django 3.2+
- SQLite (or any other database supported by Django)

For further information, refer to the official Django documentation at [djangoproject.com](https://www.djangoproject.com/).