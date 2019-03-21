from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('profile/<slug:slug>', views.OtherUserProfileView.as_view(), name='view-profile'),
]
