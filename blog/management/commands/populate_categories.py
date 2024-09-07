# demo data,  to generate , we need important library for post's data - pip install faker

from typing import Any
from blog.models import Category

from django.core.management.base import BaseCommand
    # to run with command




class Command(BaseCommand):
    help = "This command inserts category data"

    

    def handle(self, *args: Any, **options: Any) :
        Category.objects.all().delete()
        #delete existing data

        categories =[
            "Sports",'Technology' ,'Science','Art', 'Food'
        ]

        for category_name in categories:
            Category.objects.create(name = category_name)


        self.stdout.write(self.style.SUCCESS("Completed Inserting Data"))