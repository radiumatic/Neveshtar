from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


User = get_user_model()



class Command(BaseCommand):
    

    help = 'Adds the users you want to staff (provide emails)'

    def add_arguments(self, parser):
        parser.add_argument('users', nargs='+', type=int)

    def handle(self, *args, **options):
        for email in options['users']:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise CommandError(f'User with email {email} does not exist')
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added user {email} to staff'))
        self.stdout.write(self.style.SUCCESS('Done'))
            