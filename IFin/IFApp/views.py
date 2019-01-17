from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import  login_required
from . models import Supplier, Contract, Glaccount
from .tables import SupplierTable, ContractTable, GlAccountTable
from django_tables2 import RequestConfig

# Create your views here.


def index(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    return render(request, 'IFApp/index.html', {'fulltext': fulltext})


def form(request):
    return render(request, 'IFApp/form.html')


@login_required
def glaccount(request):
    table = GlAccountTable(Glaccount.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'IFApp/glaccount.html', {'table': table})


@login_required
def contract(request):
    table = ContractTable(Contract.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'IFApp/contract.html', {'table': table})


@login_required
def supplier(request):
    table = SupplierTable(Supplier.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'IFApp/supplier.html', {'table': table})
