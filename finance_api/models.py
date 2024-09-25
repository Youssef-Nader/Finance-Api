from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    transaction_date = models.DateField(default=timezone.now)
    transaction_description = models.TextField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    selected_users = [
        (1, '1- Ali Osman'),
        (2, '2- Mohamed Abdo'),
        (3, '3- Mohamed Yasser'),
    ]
    user_id = models.IntegerField(choices=selected_users, default=1)
    def __str__(self):
        return self.transaction_description