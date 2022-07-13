# Neveshtar
# Copyright (C) 2022  Nima Ghasemi Por
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This file contains functions which are not worthy to create a seperate file
And/or are not standard to be included in used-in files
"""
from dotenv import load_dotenv
from os.path import exists, join
from os import environ
def string_to_boolean(str:str):
    return True if str.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh'] else False
def load_envs(parent_dir:str):
    if exists(join(parent_dir, '.env')):
        environ["DEBUG"] = "True"
        load_dotenv()
        


        