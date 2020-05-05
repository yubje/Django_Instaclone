from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/follow', views.follow, name='follow'),
    path('<username>/follow_list/', views.follow_list, name='follow_list'),
]