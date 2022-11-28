from django.urls import path
from .views Import ProfileListView, ProfileDetailView, FollowView

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list-view'),
    path('friends/<int:pk>', FollowView, name='profile-follow'),
    path('<pk>/', ProfileDetailView.as_view(), name='profile-detail-view')
]