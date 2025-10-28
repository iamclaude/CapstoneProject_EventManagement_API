from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListCreate.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
