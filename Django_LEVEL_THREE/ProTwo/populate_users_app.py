import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

# FAKE POP SCRIPT
from Users.models import users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        #Create the fake first name , last name and email
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        new_user = users.objects.get_or_create(first_name=fake_first_name, last_name= fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print('Population done')
