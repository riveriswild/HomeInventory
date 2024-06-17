from django.db import models


class GeneralItem(models.Model):
    ''' Describes a general item in inventory'''
    purchased_at = models.DateTimeField(auto_now_add=True)
    purchase_place = models.CharField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(upload_to="images/")
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=256)  # maybe linked model
    comments = models.TextField(blank=True, null=True)


# Create your models here.
