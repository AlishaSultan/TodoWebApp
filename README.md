How to Start and use Web App:

•	First you need to install python and check version of python in cmd

 

Create a Django project. I'll provide a reference link where you can find help, and you can also follow my steps
https://www.geeksforgeeks.org/how-to-create-a-django-project/

Create Django Project:

Open the command prompt (cmd) and create a directory named 'django_project.' Ensure that the name matches exactly because it will be our project name



 
Navigate to the Django_Project directory using the `cd` command. Here, you’ll find all the necessary components to get your project up and running.

 


 Creating the Virtual Environment

   python -m venv myproject

 


Activating the Virtual Environment
venv\Scripts\activate

 



 Installing Django
  
pip install Django 

 


Once the installation is complete, you must verify that Django has been successfully installed. To do this, enter the following command:
django-admin --version
 




Create the Django Project

Create the project using the following command:
django-admin startproject todo

Change into the test_project directory:
Cd todo

Create app in Django
django-admin startapp todoApp





Close cmd and open project in VS code. Open Terminal and run:

 

 

 

If you get this error then run:
 

Active Environment:
 


Start Server:
 

http://127.0.0.1:8000/ click on this url ….you get this after running the server

 

How to use project:
If you want your tasks to be saved, first log out and create your new account by signing up or logging in. In the signup process, all validations are applied: the username must be unique and not already in use, the email must be valid, the password must be strong, and in the backend, the password will be saved as hashed. The confirm password field should match the first password, and if any field is left empty, an error message will be displayed prompting to fill in all the fields. Once the account is successfully created, a message confirming this will appear. Then, proceed to log in. If the username or password is incorrect, an error message will be displayed, and if correct, the user will be directed to the dashboard.
In the dashboard, there is a navigation bar containing options to log out and switch between light and dark mode. Then, you can add a new task by providing a title, description (up to 200 words), status (complete or pending), priority, deadline date, and time. Once the task is added, it will be stored in the backend.
When you log out and log back in, the task will still be there. To view tasks, you can click on "see task," where the background color will be based on priority. In the actions section, you can edit, delete, or change the status of the task. Additionally, after 30 minutes, a notification will remind you that your task is pending and needs to be completed. Upon page refresh, an automated notification reminder will also appear, displaying the task name, deadline, and time. Additionally, there is a tour available to guide you on how to use the app.

















