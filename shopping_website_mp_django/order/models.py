from django.contrib.auth.models import User
from django.db import models

from book.models import Book, Author

from django.conf import settings



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True,  null=True)
    email = models.CharField(max_length=100, blank=True,  null=True)
    address = models.CharField(max_length=100, blank=True,  null=True)
    phone = models.CharField(max_length=100, blank=True,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.full_name or ''

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id or ''
