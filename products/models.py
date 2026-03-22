from django.db import models
import uuid
from django.utils import timezone

class BaseModel(models.Model):

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

    def __str__(self):
        return self.name

    def average_rating(self):
        pass



class Blog(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title



class Posts(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)



    def __str__(self):
        return self.title
