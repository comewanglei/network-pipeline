from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
import project_name.serializer_user


User = get_user_model()


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = project_name.serializer_user.UserSerializer
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
# end of UserViewSet
