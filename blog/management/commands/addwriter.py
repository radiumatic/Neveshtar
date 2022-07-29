# Neveshtar
# Copyright (C) 2022  radiumatic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


User = get_user_model()



class Command(BaseCommand):
    

    help = 'Adds the users you want to writers (provide emails)'

    def add_arguments(self, parser):
        parser.add_argument('users', nargs='+', type=str)

    def handle(self, *args, **options):
        Writers = Group.objects.get(name='Writers')
        for email in options['users']:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise CommandError(f'User with email {email} does not exist')
            Writers.user_set.add(user)
            self.stdout.write(self.style.SUCCESS(f'Successfully added user {email} to writers'))
        self.stdout.write(self.style.SUCCESS('Done'))
            