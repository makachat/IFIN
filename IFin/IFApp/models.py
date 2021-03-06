from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_user_modify = models.ForeignKey(User, default='1', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Supplier(TimespamtedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.description)

    class Meta:
        ordering = ('name',)


class Glaccount(TimespamtedModel):
        glaccount = models.DecimalField(max_digits=8, decimal_places=0)
        description = models.CharField(max_length=50)

        def __str__(self):
            return 'GL Account : {}-{}'.format(self.glaccount, self.description)

        class Meta:
            ordering = ('glaccount',)


class Site(TimespamtedModel):
    country = (
        ('CA', 'CANADA'),
        ('US', 'USA')
    )
    category = (
        ('Plant', 'Plant'),
        ('DataCenter', 'Data Center'),
        ('Yard', 'Yard'),
        ('DistributionCenter', 'Distribution Center'),
        ('HeadOffice', 'Head Office')
    )

    site = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=10, choices=country, blank=True, null=True)

    def __str__(self):
        return '{} - {} with Category type :{} Modify by : {}'.format(self.site, self.country, self.category, self.last_user_modify)

    class Meta:
        ordering = ('site',)


class Contract(TimespamtedModel):
    entityChoice = (
        ('SJ-INC', 'Stella-Jones INC'),
        ('MCHI', 'MacFarland'),
        ('SJ-CORP', 'Stella-Jones Corporate')
    )
    typeOfExpenseChoice = (
        ('Capex', 'Capex'),
        ('Opex', 'Opex')
    )
    currencyChoice = (
        ('CAD', 'CAD'),
        ('USD', 'USD')
    )

    entity = models.CharField(max_length=10, choices=entityChoice)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    glaccount = models.ForeignKey(Glaccount, on_delete=models.PROTECT)
    typeOfExpense = models.CharField(max_length=10, choices=typeOfExpenseChoice)
    description = models.TextField()
    reference = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    renewalDate = models.DateField(null=True , blank=True)
    monthlyCost = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, choices=currencyChoice)
    noticePeriod = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    siteAffectation = models.ForeignKey(Site, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return 'Contract : {} - {} : '.format(self.supplier, self.reference, self.description)

    class Meta:
        ordering = ('supplier',)










