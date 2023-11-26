from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api

urlpatterns =[
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    path('', views.home, name="home"),
    path('', views.sidemenu, name="sidemenu"),

    path('settingsapp/', views.settingsapp, name="settingsapp"),
    path('profile/', views.profile, name="profile"),
    path('update-user/', views.updateUser, name="update-user"),
    
    path('api/learning-data/', api.learning_data_list, name='learning-data-list'),
    path('api/learning-data/create/', api.learning_data_create, name='learning-data-create'),
    path('api/learning-data/<int:pk>/', api.learning_data_detail, name='learning-data-detail'),

]