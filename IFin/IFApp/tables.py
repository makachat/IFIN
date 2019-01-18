from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_tables2 as tables

from .models import Supplier, Contract, Glaccount


class SupplierTable(tables.Table):
    class Meta:
        model = Supplier
        sequence = ('id', 'name', 'description', 'created_at', 'updated_at')
        template_name = 'django_tables2/bootstrap.html'


class ContractTable(tables.Table):
    class Meta:
        model = Contract
        template_name = 'django_tables2/bootstrap.html'


class GlAccountTable(tables.Table):
    class Meta:
        model = Glaccount
        template_name = 'django_tables2/bootstrap.html'

