from rest_framework import serializers
from ..models import Talk


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = (
            'name',
            'description',
            'speaker',
            'url',
            'number_of_views',
            'transcript',
        )
