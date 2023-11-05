from rest_framework import serializers
from datetime import datetime
from .models import Item


# class ItemSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(min_length=20)
#     price = serializers.IntegerField()
#     is_active = serializers.BooleanField(default=True)
#     created_at = serializers.DateTimeField(default=datetime.now())
#     updated_at = serializers.DateTimeField(default=datetime.now())
#
#     def create(self, validated_data):
#         item = Item.objects.create(name=validated_data.get('name', None),
#                                    description=validated_data.get('description', None),
#                                    price=validated_data.get('price', 0),
#                                    is_active=validated_data.get('is_active', True),
#                                    created_at=validated_data.get('created_at', datetime.now()),
#                                    updated_at=validated_data.get('updated_at', datetime.now())
#                                    )
#         item.save()
#         return item
#
class ItemSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(default=datetime.now())
    updated_at = serializers.DateTimeField(default=datetime.now())
    class Meta:
        model = Item
        # fields = '__all__'
        fields = ('name', 'description', 'price', 'is_active', 'created_at', 'updated_at')

