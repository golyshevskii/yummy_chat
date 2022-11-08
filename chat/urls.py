from django.urls import path
from django.contrib.auth import views
from .views import sign_up, rooms, room


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='base.html'), name='login'),
    path('signup/', sign_up, name='signup'),
    path('', views.LogoutView.as_view(), name='logout'),
    path('rooms/', rooms, name='rooms'),
    path('<slug:slug>/', room, name='room')
]