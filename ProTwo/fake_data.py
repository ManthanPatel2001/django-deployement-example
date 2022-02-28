import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
import django
django.setup()

from faker import Faker
from AppTwo.models import user

fakegen = Faker()

def user_details(N = 5):

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first = fake_name[0]
        fake_last = fake_name[1]
        fake_email = fakegen.email()

        # Create new Webpage Entry
        user_detail = user.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]


if __name__ == '__main__':
    print("Your Data is Processing")
    user_details(20)
    print('successful')