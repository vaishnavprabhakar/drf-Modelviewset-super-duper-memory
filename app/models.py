from django.db import models

# Create your models here.


class Product(models.Model):

    product_name = models.CharField(max_length=50)

    available = models.BooleanField(default=True)


    def __str__(self):
        return self.product_name
    
    