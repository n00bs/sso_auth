from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers


class AuthorizationTokenSerializer(QuerySetReadableMixin, serializers.Serializer):
    account = serializers.HyperlinkedRelatedField(
        queryset=Account.objects.all(),
        required=True,
        view_name='api:account-detail',
    )

    class Meta:
        fields = ['account']
