from rest_framework import serializers
from app.models import clients


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = clients
        fields = ('user','entry')