from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from core.models import (
    Team,
    Part,
    Aircraft
)
from rent_iha import serializers


class TeamViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.TeamSerializer
    queryset = Team.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TeamSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        responsible_part_type = serializer.validated_data.get("responsible_part_type")

        if not responsible_part_type:
            raise ValueError("A responsible part type must be provided for the team.")
        
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'team',
                OpenApiTypes.STR,
                description='Comma separated list of team IDs to filter',
            ),
        ]
    )
)
class PartViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.PartSerializer
    queryset = Part.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def _params_to_ints(self, qs):
        """Convert a list of strings to integers."""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        team = self.request.query_params.get('team')
        queryset = self.queryset
        if team:
            int_team_id = int(team)
            queryset = queryset.filter(team_id=int_team_id)

        return queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PartSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        team = self.request.user.team
        if not team:
            raise ValueError("User team is not setted. Please set user's team before creating a part.")
        if team.responsible_part_type != serializer.validated_data['part_type']:
            raise ValueError(f"Your team cannot produce parts of type '{serializer.validated_data['part_type']}'")
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'part',
                OpenApiTypes.STR,
                description='Comma separated list of part IDs to filter',
            ),
        ]
    )
)
class AircraftViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AircraftSerializer
    queryset = Aircraft.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        part = self.request.query_params.get('part')
        queryset = self.queryset
        if part:
            int_team_id = int(part)
            queryset = queryset.filter(part_ids=int_team_id)

        return queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AircraftSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        aircraft_name = serializer.validated_data.get("aircraft_name")

        if not aircraft_name:
            raise ValueError("Aircraft name is not given.")
        
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
