from django.db import models


class Location(models.Model):
    """Tree-like location structure within the house"""

    name = models.CharField(max_length=256)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )

    def __str__(self):
        return self.name


class GeneralItem(models.Model):
    """Describes a general item in inventory"""

    purchased_at = models.DateTimeField(auto_now_add=True)
    purchase_place = models.CharField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(upload_to="images/")
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    comments = models.TextField(blank=True, null=True)


# Create your models here.
