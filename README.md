## Django CRUD Application for School Data
#### This Django application provides basic CRUD (Create, Read, Update, Delete) operations for managing school data such as name, principal, and location.

# Features
Create: Add new schools with their details.
Read: View a list of all schools and their details. View details of individual schools.
Update: Modify the details of existing schools.
Delete: Remove schools from the database.
Technologies Used
Django: Python web framework used for backend development.
SQLite: Default database engine provided by Django for development.
Bootstrap: Used for styling and frontend components.
Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone <repository_url>
cd django-crud-school   
Create a virtual environment:

bash
Copy code
python -m venv env
Activate the virtual environment:

On Windows:
bash
Copy code
.\env\Scripts\activate
On macOS/Linux:
bash
Copy code
source env/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser (admin):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open a web browser and go to http://localhost:8000/ to view the application.

Usage
Admin Interface: Use the Django admin interface at http://localhost:8000/admin/ to manage school data.
CRUD Operations: Use the provided views to perform CRUD operations on school data.
File Structure
markdown
Copy code
django-crud-school/
├── README.md
├── manage.py
├── requirements.txt
├── schoolapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── ...
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── templates/
    └── schoolapp/
        ├── school_list.html
        ├── school_detail.html
        ├── school_form.html
        └── base.html
Contributing
Contributions are welcome! Please fork the repository and create a pull request for any new features or fixes.


