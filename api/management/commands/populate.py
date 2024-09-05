import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import *

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with random sample data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting previous data...'))
        RegisteredUser.objects.all().delete()
        Contacts.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating new sample data...'))

        # Create registered users
        for _ in range(50):  # Adjust the number of users as needed
            user = RegisteredUser.objects.create_user(
                username = fake.user_name(),
                email= fake.email(),
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                password=fake.password(),
                phone_number = fake.phone_number(),
            )

            # Create contacts for each user
            for _ in range(random.randint(1, 5)):
                Contacts.objects.create(
                    user=user,
                    first_name = fake.first_name(),
                    last_name = fake.last_name(),
                    phone_number = fake.phone_number(),
                    email = fake.email(),
                    is_spam = fake.boolean(),
                )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
