## Project Description

This project is a web application built using Django, a high-level Python web framework. The main goal of the application is to provide users with personalized product recommendations based on their past purchases.

### How to Use


1. Install Dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set Up the Database:
   - Ensure you have PostgreSQL installed and running.
   - Create a new PostgreSQL database for the project.
   - Update the database settings in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '',
         }
     }
     ```

4. Run Migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a Superuser:
   ```
   python manage.py createsuperuser
   ```

6. Load Sample Data (Optional):
   ```
   python manage.py loaddata sample_data.json
   ```

7. Run the Development Server:
   ```
   python manage.py runserver
   ```

8. Access the Application:
   - Open your web browser and go to `http://127.0.0.1:8000/` to access the application.
   - Create user account make some purchases and after ur next login u will see recomendation.
   - Create and log in with the superuser account and make admin from normal user to see admin dishboard.
   - Explore the platform, add products to the shopping basket, and view personalized recommendations.
