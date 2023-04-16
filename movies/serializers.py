from rest_framework import serializers
from movies.models import CategoryMovie, Movie
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(
        choices=CategoryMovie.choices,
        default=CategoryMovie.G,
    )
    synopsis = serializers.CharField(default=None)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
