from datetime import timezone

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    old_price = models.DecimalField(decimal_places=2, max_digits=10)
    new_price = models.DecimalField(decimal_places=2, max_digits=10)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    is_sale = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Co(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()
    with_c = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.email