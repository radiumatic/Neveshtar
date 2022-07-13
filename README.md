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
1. Clone this repository (`git clone https://github.com/nimagp/Neveshtar)
2. [Create a project](https://devcenter.heroku.com/articles/creating-apps)
3. Set the variables mentioned before using [this](https://devcenter.heroku.com/articles/config-vars) way or Heroku dashboard
4. Add these lines to the file Neveshtar/sttings.py (make sure you add them before the statement `import django_on_heroku`, preferably after `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`):

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
   heroku run python manage.py createsuperuser
   ```
   It will ask you in order for Email, Username, Name, Last name, and password
8. Create a user group with these permissions in heroku admin(a tutorial can be found here) 
Done. Enjoy!
### PC/VPS
The steps are even simpler:
1. Install Python if you don't have it already
2. Clone this repository (`git clone https://github.com/nimagp/Neveshtar)
3. Create a Virtual Environment and enable it using these commands:
   ```bash
   #Windows
   python -m venv .venv
   .venv\Scripts\activate
   #Linux and Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Add variables using `.env` file. Please notice that you should name the file exactly the same

   Use this pattern and add all the variables:
   ```
   Variable = "Value"
   ```
5. Install required packages using this command:
   ```bash
   pip install -r requirements.txt
   ```
6. Run these commands in order to prepare database:
   ```bash
   python manage.py makemigrations
   python manage.py makemigrations blog
   python manage.py makemigrations accounts
   python manage.py migrate
   ```
7. Create a SuperUser to moderate the blog with this command:

   ```bash
   python manage.py createsuperuser
   ```
   It will ask you in order for Email, Username, Name, Last name, and password

8. Run server with this command:
   ```bash
   python manage.py runserver
   ```
9. **FOR VPS**, You should configure a web server too. You can follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps), but please change the details to make sure it's compatible with this project.

## Known issues
* If you enter invalid (not incorrect, invalid) information in registering, resetting password and login forms, it just returns you to the form without any error
* Wrong favicon
* Too fast like and dislike, knocks like and comment script up, and you can't put like or comment until you refresh the page

These will be fixed.

## Why this name?
Neveshtar means writing in Persian.

## License
AGPL 3.0 
You can find full text in LICENSE file





