from rest_framework import serializers
from .models import Photography
from .validations import *

class PhotographySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Photography
        fields = ['id', 'name', 'subtitle', 'description', 'category', 'photo', 'date', 'published']

    def get_category(self, obj):
        return obj.get_category_display()

    def validate(self, data):
        if not valid_subtitle(data['subtitle']):
            raise serializers.ValidationError('The subtitle must have at least 10 characters!')
        if not valid_description(data['description']):
            raise serializers.ValidationError('The description must have at least 20 characters!')
        return data
