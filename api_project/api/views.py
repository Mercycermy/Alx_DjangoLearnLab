from .serializers import BookSerializer, UserSerializer
from .models import Book
from rest_framework import generics, viewsets, permissions, views 
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



User = get_user_model()
# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TokenObtainView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get or create a token for the authenticated user
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({
            "token": token.key,
            "created": created,  # True if the token was just created
        })
class UserViewSet(viewsets.ModelViewSet):
    """Following Tutorials on REST page
        API EndPoint to allow users to be viewed or edited"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly] 