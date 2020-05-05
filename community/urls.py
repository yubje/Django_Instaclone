from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<article_pk>/', views.detail, name='detail'),
    path('<article_pk>/update/', views.update, name='update'),
    path('<article_pk>/delete/', views.delete, name='delete'),
    path('<article_pk>/comments_create', views.comments_create, name='comments_create'),
    path('<article_pk>/<comment_pk>/comments_delete', views.comments_delete, name='comments_delete'),
    path('<article_pk>/like/', views.like, name='like'),
    path('<article_pk>/like_list/', views.like_list, name='like_list'),

]