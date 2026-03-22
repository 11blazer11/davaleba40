from django.db import models
from django.core.validators import MaxValueValidator
import uuid
from django.utils import timezone

class BaseModel(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,)

    created_at = models.DateTimeField(db_index=True, default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    CURRENCY_CHOICES = [
        ('GEL', 'GEL'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]
        
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField()

    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='GEL'
    )

    tags = models.ManyToManyField("products.ProductTag", related_name='products', blank=True)

    def __str__(self):
        return self.name

    def average_rating(self):
        pass

    