from django.core.management.base import BaseCommand
import csv
import random


class Command(BaseCommand):
    help = 'Generate a CSV file with sample data'

    def handle(self, *args, **kwargs):
        products = [
            {"name": "Laptop", "description": "14-inch, 8GB RAM, 256GB SSD",
                "category": "Electronics"},
            {"name": "Bookshelf", "description": "Wooden 5-tier shelf",
                "category": "Furniture"},
            {"name": "Running Shoes", "description": "Size 10, Breathable Mesh",
                "category": "Clothing"},
            {"name": "LED Light Bulb", "description": "60W Equivalent, Soft White",
                "category": "Home Goods"},
            {"name": "Guitar", "description": "Acoustic, Natural Finish",
                "category": "Musical Instruments"},
            {"name": "Blender", "description": "500W, 3-speed",
                "category": "Appliances"},
            {"name": "Backpack", "description": "Water-resistant, 20L capacity",
                "category": "Accessories"},
            {"name": "Wristwatch", "description": "Analog, Leather Strap",
                "category": "Fashion"},
            {"name": "Mobile Phone", "description": "5.5-inch display, 64GB",
                "category": "Electronics"},
            {"name": "Desk Chair", "description": "Ergonomic, Adjustable height",
                "category": "Furniture"}
        ]
        with open('ecommerce_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'description','stock','price','category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(100):
                product = random.choice(products)
                writer.writerow({
                    'name': product['name'],
                    'description': product['description'],
                    'stock': random.randint(0, 100),
                    'price': random.randint(10, 1000),
                    'category': product['category']
                })
        self.stdout.write(self.style.SUCCESS('Successfully generated CSV file'))
