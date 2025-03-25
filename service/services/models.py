from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()
    

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Базовый'),
        ('student', 'Студент'),
        ('business', 'Бизнес'),
    )
    
    plan_type = models.CharField(max_length=10, choices=PLAN_TYPES)
    discount_percent = models.PositiveIntegerField(default=0, 
                                                   validators=[
                                                       MaxValueValidator(100)
                                                       ])


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="subscriptions")
    