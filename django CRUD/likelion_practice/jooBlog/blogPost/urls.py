from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:post_id>/delete', views.delete, name='delete'),
    path('<int:post_id>/update', views.update, name='update'),
    path('fake/', views.fake, name='fake'),
]