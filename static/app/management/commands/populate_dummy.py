from django.core.management.base import BaseCommand
from app.models import Company, Nanny


class Command(BaseCommand):
    help = 'Populate database with dummy companies and nannies for UI testing'

    def handle(self, *args, **options):
        # Clear existing sample companies (only those we create here)
        sample_names = ['Little Stars', 'HappyHands Nannies', 'BrightKids Care']
        for name in sample_names:
            Company.objects.filter(name=name).delete()

        companies = []
        companies.append(Company.objects.create(
            name='Little Stars',
            description='Small local nanny agency specialising in newborn and infant care.',
            location='Nairobi',
            phone_number=+254711111111,
            email='contact@littlestars.example'
        ))
        companies.append(Company.objects.create(
            name='HappyHands Nannies',
            description='Trusted part-time and full-time nannies for busy families.',
            location='Mombasa',
            phone_number=+254722222222,
            email='info@happyhands.example'
        ))
        companies.append(Company.objects.create(
            name='BrightKids Care',
            description='Professional, certified caregivers with early childhood experience.',
            location='Kisumu',
            phone_number=+254733333333,
            email='hello@brightkids.example'
        ))

        # Create sample nannies for each company
        for company in companies:
            for i in range(1,4):
                Nanny.objects.create(
                    name=f"{company.name.split()[0]} Nanny {i}",
                    experience=f"{1 + i} years",
                    rates=1000 + i * 250,
                    availability=True,
                    age=25 + i,
                    location=company.location,
                    about=f"Experienced nanny ({i}) from {company.name} with background in childcare.",
                    skills='feeding, bathing, playtime, early education',
                    company=company
                )

        self.stdout.write(self.style.SUCCESS('Dummy companies and nannies created.'))
