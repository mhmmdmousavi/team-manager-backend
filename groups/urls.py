from django.urls import path
from .views import GroupListView, GroupDetailView

urlpatterns = [
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
]
