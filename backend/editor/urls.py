from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DocumentListCreateView, DocumentDetailView, TagListView, UserRegistrationView

urlpatterns = [
    # Authentication endpoints
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Document endpoints
    path('api/documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('api/documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    
    # Tag endpoints
    path('api/tags/', TagListView.as_view(), name='tag-list'),
]
