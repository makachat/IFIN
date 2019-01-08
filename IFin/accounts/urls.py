from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_ifapp, name='login'),
    path('logout', views.logout_ifapp, name='logout'),

]
