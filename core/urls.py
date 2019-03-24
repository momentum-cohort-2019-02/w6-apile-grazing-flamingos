from django.urls import path
# from django.conf.urls import url
from . import views
from core.views import UserPost


urlpatterns = [
    path('', views.HomePageView.as_view(model=UserPost), name='index'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('<slug:slug>/', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('codeofconduct/', views.CCView.as_view(), name='codeofconduct'),
    path('post_detail/<slug:slug>', views.post_detail_view, name ='post_detail'),
    path('post_vote/<slug:slug>', views.post_detail_view, name ='post_vote'),
]
