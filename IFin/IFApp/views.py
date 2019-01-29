from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import  login_required
from . models import Supplier, Contract, Glaccount, Site
from .tables import SupplierTable, ContractTable, GlAccountTable, SiteTable
from django_tables2 import RequestConfig
from django.utils import timezone

# Create your views here.


def index(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    return render(request, 'IFApp/index.html', {'fulltext': fulltext})


def form(request):
    return render(request, 'IFApp/form.html')


@login_required
def glaccount(request):
    glaccountlist = Glaccount.objects.all()
    return render(request, 'IFApp/glaccount.html', {'glaccountlist': glaccountlist})

@login_required
def contract(request):
    contratList = Contract.objects.all()
    return render(request, 'IFApp/contract.html', {'contratList': contratList})


@login_required
def supplier(request):
    supplierList = Supplier.objects.all()
    return render(request, 'IFApp/supplier.html', {'supplierList': supplierList})


@login_required
def site(request):
    siteList = Site.objects.all()
    return render(request, 'IFApp/site.html', {'siteList': siteList})


@login_required
def addsite(request):
    if request.method == 'POST':
        if request.POST['site'] and request.POST['category']:
            site = Site()
            site.site = request.POST['site']
            site.category = request.POST['category']
            site.country = request.POST['country']
            site.address = request.POST['address']
            # outside the form
            site.created_at = timezone.datetime.now()
            site.updated_at = timezone.datetime.now()
            site.last_user_modify = request.user
            site.save()
            return redirect('home')
        else:
            return render(request, 'IFApp/addsite.html')
    else:
          return render(request, 'IFApp/addsite.html')


@login_required
def testsite(request, i):
    return render(request, 'IFApp/testsite.html', {'i': i})

