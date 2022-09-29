# Neveshtar
### A simple (Persian) blog, with support of signing up by other users, markdown, and multiple writers

## Why this exists?
Because, Why not?

## Installation 
### Requirements 
Steps are different for PC/VPS and Heroku. But for both of them, You need to prepare an SMTP server.

SMTP server is needed for account management system. If you don't know what SMTP is, check out [this](https://medium.com/@jonathansychan/smtp-simple-mail-transfer-protocol-ed443b1f51d7) for a detailed explaining, and [this](https://medium.com/@pepipost/what-is-smtp-9503c52760e4) for a just-want-to-know-what-does-this-stands-for explaining

If you just want to test this on your own PC, consider using some dummy SMTP server like [smtp4dev](https://github.com/rnwood/smtp4dev)(offline) or [Mailtrap dummy email server](https://mailtrap.io/fake-smtp-server/)(online) (plenty out there)

If you want to use Neveshtar in production and present it to public, You should use a proper SMTP provider (some free ones are elasticemail and gmail). If you just want to test it in production (which I don't understand why you would), You can use something like Mailtrap.

You need these variables in the next steps:

* SMTP_HOST

   IP / Address of the SMTP server 

* SMTP_PORT

   Port of running SMTP server 

* USE_TLS_SMTP

   Your provider specifies this, But originally it's true. If your provider does not support TLS **OR** you are using an offline dummy SMTP server like smtp4dev, set this to "False".

   Otherwise, choose between one of these words (capital alphabets or not): 
   1. True
   2. 1 
   3. T
   4. Y
   5. Yes
   6. Yeah
   7. Yup
   8. Certainly
   9. Uh-huh

* SMTP_USERNAME 

   Username of your SMTP account (credentials, **this is different** from your account at provider site)

* SMTP_PASSWORD 

   Password of your SMTP account (credentials, **this is different** from your account at provider site)

* EMAIL_HOST_USER

   The email address that is used when sending emails.

   Be careful about this. This is the address users see in their inbox

* SECRET_KEY

   As Django official documentation says:

   > A secret key used to provide cryptographic signing, and should be set to a unique, unpredictable value.

   > ...

   > Running Django with a known SECRET_KEY defeats many of Django’s security protections, and can lead to privilege escalation and remote code execution vulnerabilities.  

   You can generate a key using [this](https://djecrety.ir/) tool (safe to use)

You can use any database Django supports (or can support with plugins) but usually defaults (sqlite3 for PC/VPS and PostgreSQL for Heroku) are enough.
   

### Heroku
The steps are pretty simple:
1. Clone this repository (`git clone https://github.com/nimagp/Neveshtar`)
2. [Create a project](https://devcenter.heroku.com/articles/creating-apps)
3. Set the variables mentioned before using [this](https://devcenter.heroku.com/articles/config-vars) way or Heroku dashboard
4. Add these lines to the file Neveshtar/settings.py (make sure you add them before the statement `import django_on_heroku`, preferably after `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`):

   ```python
   CSRF_TRUSTED_ORIGINS = [
    'https://example.herokuapp.com'
   ]
   ```
   Rename example to your Heroku project name
5. Commit changes to git and run this command to make sure you have Heroku git remote configured:

   ```bash
   heroku git:remote -a example
   ```
   Change example to your Heroku project name
6. Run this command to deploy project to Heroku:

   ```bash
   git push heroku HEAD:main
   ```
7. Create a SuperUser to moderate the blog with this command:

   ```bash
   heroku run "python manage.py createsuperuser"
   ```
   It will ask you in order for Email, Username, Name, Last name, and password
8. Run this command to create Writers permissions:
   ```bash
   heroku run "python manage.py setupwriters"
   ```
9. You need to add yourself to writers with this command:
   ```bash
   heroku run "python manage.py addwriter 'example@example.com'"
   ```
   
   Change example@example.com to the email you entered in creating super user. You can give more than one email and make multiple users writer at the same time

   You should do this everytime you want to add a new writer. First, Tell that person to create an account using register form, and then run this command(same syntex as the `addwriter` command) to make him/her staff, then run the `addwriter` again with his/her email:
      ```bash
      heroku run "python manage.py addstaff 'example@example.com'"
      ```
Done. Enjoy!
### PC/VPS
The steps are even simpler:
1. Install Python if you don't have it already
2. Clone this repository (`git clone https://github.com/nimagp/Neveshtar`) and navigate to the created directory

3. Eeither run this command to configure automatically:
   ```bash
   python3 scripts/setup.py
   ```
   or follow these steps to do it yourself:
   1. Create a Virtual Environment and enable it using these commands:
      ```bash
      #Windows
      python -m venv .venv
      .venv\Scripts\activate
      #Linux and Mac
      python3 -m venv .venv
      source .venv/bin/activate
      ```
   2. Add variables using `.env` file. Please notice that you should name the file exactly the same

      Use this pattern and add all the variables:
      ```
      Variable = "Value"
      ```
   3. Install required packages using this command:
      ```bash
      pip install -r requirements.txt
      ```
   4. Run these commands in order to prepare database:
      ```bash
      python3 manage.py makemigrations
      python3 manage.py makemigrations blog
      python3 manage.py makemigrations accounts
      python3 manage.py migrate
      ```

   5. Run this command to create Writers permissions:
      ```bash
      python3 manage.py setupwriters
      ```
   6. Create a SuperUser to moderate the blog with this command:

      ```bash
      python3 manage.py createsuperuser
      ```
      It will ask you in order for Email, Username, Name, Last name, and password

4. Enable virtual environment for two next commands:

   Windows:
   ```cmd
   .venv\Scripts\activate
   ```
   Linux:
   ```bash
   source .venv/bin/activate
   ```

5. You need to add yourself to writers with this command:
   ```bash
   python3 manage.py addwriter 'example@example.com'
   ```
   
   Change example@example.com to the email you entered in creating super user. You can give more than one email and make multiple users writer at the same time

   You should do this everytime you want to add a new writer. First, Tell that person to create an account using register form, and then run this command(same syntex as the `addwriter` command) to make him/her staff, then run the `addwriter` again with his/her email:
      ```bash
      python3 manage.py addstaff 'example@example.com'
      ```

6. Run server with this command:
   ```bash
   python3 manage.py runserver
   ```
7. **FOR VPS**, Add these lines to the file Neveshtar/settings.py (make sure you add them before the statement `import django_on_heroku`, preferably after `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`):

   ```python
   CSRF_TRUSTED_ORIGINS = [
    'https://your-address.com/'
   ]
   ```
   Change https://your-address.com to the IP/Address of your VPS

8. **FOR VPS**, You should configure a web server too. You can follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps), but please change the details to make sure it's compatible with this project.

## Known issues
* If you enter invalid (not incorrect, invalid) information in registering, resetting password and login forms, it just returns you to the form without any error
* Wrong favicon
* Too fast like and dislike, knocks like and comment script up, and you can't put like or comment until you refresh the page

These will be fixed.

## Why this name?
Neveshtar means writing in Persian.

## License
GPLv3
You can find full text in LICENSE file





