from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('supplier', views.supplier, name='supplier'),
    path('contract', views.contract, name='contract'),
    path('glaccount', views.glaccount, name='glaccount'),
]

