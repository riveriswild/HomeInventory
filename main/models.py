from django.db import models


class Location(models.Model):
    ''' Tree-like location structure within the house '''

    name = models.CharField(max_length=256)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )

    def __str__(self):
        return self.name

    def get_ancestors(self):
        ''' Returns all ancestors of the location '''
        ancestors = []
        location = self
        while location.parent is not None:
            location = location.parent
            ancestors.append(location)
        return ancestors

    def get_descendants(self):
        ''' Returns all descendants of the location '''
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants


class GeneralItem(models.Model):
    ''' Describes a general item in inventory '''

    purchased_at = models.DateTimeField(auto_now_add=True)
    purchase_place = models.CharField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    comments = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=356)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.track_price_history()

    def track_price_history(self):
        if self.price:
            PriceHistory.objects.create(item=self, price=self.price)


class PriceHistory(models.Model):
    ''' Tracks price changes for an item '''
    item = models.ForeignKey(GeneralItem, on_delete=models.CASCADE)
    price = models.IntegerField()
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - ${self.price} at {self.date_recorded}"


class FoodItem(GeneralItem):
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.name} (Food)"

class ClothingItem(GeneralItem):
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (Clothing)"

class FurnitureItem(GeneralItem):
    dimensions = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (Furniture)"

class ApplianceItem(GeneralItem):
    warranty_expiration = models.DateField()

    def __str__(self):
        return f"{self.name} (Appliance)"


# Create your models here.
