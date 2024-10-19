# Contact App

This is a simple web-based Contact Management application built using the Django framework. The app allows users to create, view, update, and delete contact information, including names, phone numbers, email addresses, and more.

## Features

- Add new contacts with fields like name, phone number, email, and address.
- View a list of all saved contacts.
- Edit existing contact information.
- Delete contacts from the contact list.
- Search for contacts by name or phone number.
- Responsive design for mobile and desktop users.

## Technologies Used

- **Django**: Web framework used for backend.
- **SQLite**: Default database for storing contact information.
- **HTML/CSS**: For front-end structure and styling.
- **JavaScript (optional)**: For dynamic functionality.
  
## Requirements

To run this project, you will need:

- **Python 3.x**: Make sure you have Python installed.
- **Django 4.x**: Install Django with the following command:

  ```bash
  pip install django
Installation
Clone the repository:

bash

git clone https://github.com/yourusername/contact-app.git
cd contact-app


Create a virtual environment (recommended):
bash

python -m venv env
source env/bin/activate  # For Linux/Mac
.\env\Scripts\activate   # For Windows


Install required dependencies:
bash

pip install -r requirements.txt


Run migrations:
bash

python manage.py migrate


Create a superuser (for admin access):
bash

python manage.py createsuperuser
Follow the prompts to set up your admin account.



Run the Django development server:
bash

python manage.py runserver
Open your browser and go to http://127.0.0.1:8000 to access the Contact App.


Project Structure
php
contact-app/
│
├── contacts/             # Main application folder
│   ├── migrations/       # Database migrations
│   ├── static/           # Static files (CSS, JavaScript, etc.)
│   ├── templates/        # HTML templates
│   ├── views.py          # Views for handling requests
│   ├── urls.py           # URL routing for the app
│   ├── models.py         # Contact model (database schema)
│   └── forms.py          # Django forms for creating and editing contacts
│
├── contact_app/          # Project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI entry point
│
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── README.md             # Project documentation
## Usage
### Home Page
Lists all the contacts with options to edit or delete them.
#### Add Contact
Provides a form to add a new contact. You can specify details like name, phone number, email, and address.
#### Edit Contact
Allows editing of existing contact details through a form.
#### Delete Contact
Deletes a contact from the database.
Search Functionality
Allows you to search for contacts by name or phone number.
Running Tests
To run tests for the project, you can use Django's built-in testing framework:

bash

python manage.py test
Contributing
Fork the repository.
Create a new feature branch: git checkout -b feature/your-feature-name.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/your-feature-name.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.