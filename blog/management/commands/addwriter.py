# Copyright (c) 2022 Nima Ghasemi Por
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
            