from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('supplier', views.supplier, name='supplier'),
    path('contract', views.contract, name='contract'),
    path('glaccount', views.glaccount, name='glaccount'),
    path('viewglaccount', views.viewglaccount, name='viewglaccount'),
    path('site', views.site, name='site'),
    path('addsite', views.addsite, name='addsite'),
    path('testsite/<i>', views.testsite, name='testsite'),
    path('form', views.form, name='form'),
]

