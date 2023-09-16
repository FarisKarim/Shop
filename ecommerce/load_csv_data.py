import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from shop.models import Product, Category

with open('ecommerce_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        category, created = Category.objects.get_or_create(name=row['category'])


        Product.objects.create(
            name=row['name'],
            description=row['description'],
            stock=row['stock'],
            price=row['price'],
            category=category,
        )
