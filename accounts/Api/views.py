from rest_framework.viewsets import ModelViewSet
from accounts.Api.serializers import AccountSerializer
from accounts.models import Accounts
from rest_framework.permissions import AllowAny

class AccountListCreateView(ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]
    
    http_method_names = ['get', 'put']