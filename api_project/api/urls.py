from django.db import router
from django.urls import include, path
from .views import UserViewSet, BookList, BookCreateSet, BookViewSet, TokenObtainView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  
     path('', include(router.urls)),
     path('books/create/', BookCreateSet.as_view(), name='book-create'),
     path('api-auth/', include('rest_framework.urls'), name= 'rest_framework'),

    path('token/', TokenObtainView.as_view(), name='tokens')
]