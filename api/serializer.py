from rest_framework import serializers
from webapp.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'email', 'text', 'status']


class ReviewPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['status']
