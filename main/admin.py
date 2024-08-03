from django.contrib import admin
from .models import GeneralItem, FoodItem, ClothingItem, FurnitureItem, ApplianceItem, Location


class GeneralItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "purchased_at",
        "purchase_place",
        "quantity",
        "price",
        "location",
    )
    search_fields = ("name", "purchase_place", "location__name")
    list_filter = ("purchased_at", "location")
    

class LocationAdmin(admin.ModelAdmin):
    pass


class FoodItemAdmin(GeneralItemAdmin):
    list_display = GeneralItemAdmin.list_display + ("expiration_date",)


class ClothingItemAdmin(GeneralItemAdmin):
    list_display = GeneralItemAdmin.list_display + (
        "size",
        "color",
    )


class FurnitureItemAdmin(GeneralItemAdmin):
    list_display = (
        "get_name",
        "purchased_at",
        "purchase_place",
        "quantity",
        "price",
        "location",
        "dimensions",
    )

    def get_name(self, obj):
        return obj.name

    get_name.admin_order_field = "name"
    get_name.short_description = "Name"


class ApplianceItemAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "purchased_at",
        "purchase_place",
        "quantity",
        "price",
        "location",
        "warranty_expiration",
    )
    search_fields = ("name", "purchase_place", "location__name")
    list_filter = ("purchased_at", "location", "warranty_expiration")

    def get_name(self, obj):
        return obj.name

    get_name.admin_order_field = "name"
    get_name.short_description = "Name"


# admin.site.register(FoodItem, FoodItemAdmin)
# admin.site.register(ClothingItem, ClothingItemAdmin)
admin.site.register(FurnitureItem, FurnitureItemAdmin)
admin.site.register(ApplianceItem, ApplianceItemAdmin)
admin.site.register(Location, LocationAdmin)
