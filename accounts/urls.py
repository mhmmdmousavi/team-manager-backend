from django.urls import path
from .views import ProfileListView, ProfileDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
       # JWT Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
