from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    parent_name = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ("id", "name", "parent", "parent_name", "children")

    def get_children(self, obj):
        if obj.children.exists():
            return LocationSerializer(obj.children.all(), many=True).data
        return []

    def get_parent_name(self, obj):
        return obj.parent.name if obj.parent else None
