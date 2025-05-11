from django.urls import path
from .views import TeamListView, TeamDetailView, MembershipListView

urlpatterns = [
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('memberships/', MembershipListView.as_view(), name='membership-list'),
]
