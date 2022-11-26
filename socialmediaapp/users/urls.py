from django.urls import path
from .views Import ProfileListView, ProfileDetailView,

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list-view'),
    path('switch_follow/', views.follow_unfollow_profile, name='profile-follow'),
    path('<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),
]
