from rest_framework import serializers

from core.models import (
    Team,
    Part,
    Aircraft,
    # MissingParts,
)


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for teams."""

    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ['id']


class PartSerializer(serializers.ModelSerializer):
    """Serializer for parts."""

    class Meta:
        model = Part
        fields = "__all__"
        read_only_fields = ['id']

    
class AircraftSerializer(serializers.ModelSerializer):
    """Serializer for Aircraft."""

    class Meta:
        model = Aircraft
        fields = "__all__"
        read_only_fields = ['id']


# class MissingPartsSerializer(serializers.ModelSerializer):
#     """Serializer for Aircraft."""

#     class Meta:
#         model = MissingParts
#         fields = "__all__"
#         read_only_fields = ['id']