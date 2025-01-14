Django Demo Project

Overview
This is a simple Django-based web application that demonstrates the following features:
A homepage that welcomes users.
A user form to input data (name and age).
A result page that displays the submitted data.

The project uses Django's templating system and Bootstrap for basic styling.

Features

1. Homepage
   Displays a welcome message.
   Includes a button to navigate to the form page.

2. User Form
   Accepts name and age inputs from the user.
   Performs basic validation for required fields.

3. Result Page
   Displays the submitted name and age using Django template tags.
   Provides a link to navigate back to the homepage.

Setup and Installation

1. Clone the repository:
   git clone <repository-url>
   cd <repository-folder>

2. Install dependencies:
   pip install django

3. Apply database migrations:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver

5. Open the application in your browser:
   Homepage: http://127.0.0.1:8000

How It Works

Homepage (home.html):
Greets users with a welcome message and a button to navigate to the form page.

Form Page (form.html):
Collects name and age from the user using a simple HTML form.
Sends the data to the backend upon submission.

Result Page (result.html):
Displays the submitted data using Django's template engine.

Technologies Used

Python: Core programming language for the backend.
Django: Web framework used for development.
Bootstrap:Styling framework for a responsive UI.

future Improvements
Add database integration to store user data.
Include validation for input data on the backend.
Implement user authentication and authorization.

