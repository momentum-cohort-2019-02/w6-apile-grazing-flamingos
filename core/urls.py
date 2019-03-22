from django.urls import path
from . import views
from core.views import UserPost


urlpatterns = [
    path('', views.HomePageView.as_view(model=UserPost), name='index'),
    path('profile/<slug:slug>', views.OtherUserProfileView.as_view(), name='view-profile'),

    path('username/<slug:slug>', views.UserProfileView.as_view(), name='user-profile'),
    
    path('post/new/', views.NewPostView.as_view(), name='post_new'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('codeofconduct/', views.CCView.as_view(), name='codeofconduct'),

]
