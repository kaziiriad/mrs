from rest_framework import serializers
from ..models import User, Movie, Rating

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie
        fields = '__all__'
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
    
    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

