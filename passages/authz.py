from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import authentication
from rest_framework import exceptions


class ApiKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.QUERY_PARAMS.get('api_key', None)
        if not api_key == settings.API_KEY:
            return None

        try:
            # Use the default admin user.
            user = User.objects.get(id=1)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No users in database')

        return (user, None)
