from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    path('', views.home, name="home"),
    path('', views.sidemenu, name="sidemenu"),

    path('milestone/', views.milestone, name="milestone"),
    path('settingsapp/', views.settingsapp, name="settingsapp"),
    path('profile/', views.profile, name="profile"),

]