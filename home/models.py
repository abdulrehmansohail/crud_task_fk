from django.db import models

# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='listing/icon/')
    image = models.ImageField(upload_to='listing/image/')
    address = models.CharField(max_length=100)
    status = models.BooleanField()
    rating = models.CharField(max_length=100)
    pricing = models.CharField(max_length=100)
    web = models.URLField(max_length=250)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
