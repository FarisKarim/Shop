from django.core.management.base import BaseCommand
import random
from django.contrib.auth.models import User
from shop.models import Product, Review

class Command(BaseCommand):
    help = 'Generate reviews for products'
    def handle(self, *args, **kwargs):
        reviews = [
            {"title": "Great product!", "comment": "I love this product"},
            {"title": "Not worth the money", "comment": "I would not recommend this product"},
            {"title": "Good value", "comment": "This product is a good value"},
            {"title": "Poor quality", "comment": "This product is not well made"},
            {"title": "This is a scam", "comment": "Do not buy this product"},
            {"title": "I would buy this again", "comment": "I would buy this product again. It is great! It is also very affordable"},
            {"title": "I would not buy this again", "comment": "I would not buy this product again. It is not worth the money"},
        ]
        for _ in range(100):
            rand_user = User.objects.order_by('?').first()
            rand_product = Product.objects.order_by('?').first()
            review = random.choice(reviews)
            rating = random.choice(range(1, 6))

            Review.objects.create(
                user = rand_user,
                product = rand_product,
                title = review['title'],
                comment = review['comment'],
                rating = rating
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded reviews'))