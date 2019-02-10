from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('supplier', views.supplier, name='supplier'),
    path('formsupplier', views.formSupplier, name='formSupplier'),
    path('contract', views.contract, name='contract'),
    path('formcontract', views.formContract, name='formContract'),
    path('glaccount', views.glaccount, name='glaccount'),
    path('site', views.site, name='site'),
    path('formsite', views.formSite, name='formsite'),
    path('addsite', views.addsite, name='addsite'),
    path('testsite/<i>', views.testsite, name='testsite'),

]

