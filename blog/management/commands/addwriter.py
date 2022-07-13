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
            