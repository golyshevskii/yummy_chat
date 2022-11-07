from django.urls import path
from django.contrib.auth import views
from .views import sign_up, rooms, room


urlpatterns = [
    path('', views.LoginView.as_view(template_name='base.html'), name='mainpage'),
    path('signup/', sign_up, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('rooms/', rooms, name='rooms'),
    path('<slug:slug>/', room, name='room')
]