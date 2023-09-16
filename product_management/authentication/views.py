from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from product_management.authentication.serializers import UserRegistrationSerializer
# Create your views here.
class UserRegistrationView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserRegistrationSerializer
