"""
This file contains functions which are not worthy to create a seperate file
And/or are not standard to be included in used-in files
"""
from dotenv import load_dotenv
from os.path import exists, join
def string_to_boolean(str:str):
    return True if str.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh'] else False
def load_envs(parent_dir:str):
    if exists(join(parent_dir, '.env')):
        load_dotenv()

        