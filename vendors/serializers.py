# vendor/serializers.py
from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_name(self, value):
        # Add custom validation logic for name field
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

        

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def validate_quantity(self, value):
        # Add custom validation logic for quantity field
        if value <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer.")
        return value


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')







