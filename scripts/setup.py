import os
import subprocess
print("Creating Virtualenv...")
try:
    subprocess.run(["python3 -m venv .venv"], check = True, shell=True)
    print("Done")
except Exception as err:
    print(f"There was an error : {str(err)}")
    exit()
    
python_binaries_path = r'.venv\Scripts' if os.name == "nt" else r'.venv/bin'
file_extension = ".exe" if os.name == "nt" else ""

try:
    from colorama import Fore, init, Back
except:
    try:
        print("Installing colorama...")
        subprocess.run([os.path.join(python_binaries_path, f"pip{file_extension} install colorama")], check = True, shell=True)
        print("Done")
        from colorama import Fore, init
    except Exception as err:
        print(f"There was an error : {str(err)}")
        exit()
init(autoreset=True)

print(Back.GREEN + "Installing required packages...")
try:
    subprocess.run([os.path.join(python_binaries_path, f"pip{file_extension} install -r requirements.txt")], check = True, shell=True)
    print(Fore.GREEN + "Done")
except Exception as err:
    print(Fore.RED + f"There was an error : {str(err)}")
    exit()

print(f"""{Back.GREEN}Adding environment variables...{Back.RESET}
Please see the readme to understand what you should enter""")

Variables_list = ["SMTP_HOST", "SMTP_PORT", 'USE_TLS_SMTP', 'SMTP_USERNAME', 'SMTP_PASSWORD', 'EMAIL_HOST_USER', 'SECRET_KEY']

try:
    print("Please enter the value for each of this variables:")    
    with open('.env', 'w', encoding='utf-8') as f:
        for var in Variables_list:
            value = input (f'{var} : ')
            f.write(f'{var} = "{value}"')
    print(Fore.GREEN + "Done")
except Exception as err:
    print(Fore.RED + f"There was an error : {str(err)}")
    exit()

print(Back.GREEN + 'Preparing DB...')

try:
    subprocess.run([os.path.join(python_binaries_path, f"python{file_extension} manage.py makemigrations")], check = True, shell=True)
    subprocess.run([os.path.join(python_binaries_path, f"python{file_extension} manage.py makemigrations blog")], check = True, shell=True)
    subprocess.run([os.path.join(python_binaries_path, f"python{file_extension} manage.py makemigrations accounts")], check = True, shell=True)
    subprocess.run([os.path.join(python_binaries_path, f"python{file_extension} manage.py migrate")], check = True, shell=True)
    subprocess.run([os.path.join(python_binaries_path, f"python{file_extension} manage.py setupwriters")], check = True, shell=True)

    print(Fore.GREEN + "Done")
except Exception as err:
    print(Fore.RED + f"There was an error : {str(err)}")
    exit()

print(Back.GREEN + "Creating super user(full admin)")

try:
    
    subprocess.run([os.path.join(python_binaries_path, f"python{file_extension} manage.py createsuperuser")], check = True, shell=True)
    print(Fore.GREEN + "Done")
except Exception as err:
    print(Fore.RED + f"There was an error : {str(err)}")
    exit()


print(Fore.GREEN + "Done! " + Fore.RESET + "Get back to readme.")




