from django.shortcuts import render
from rest_framework.decorators import api_view

from .forms import CompanyForm
from .models import Company


# Create your views here.
def company(request):
    form = CompanyForm()
    companies = None

    if form.is_valid():
        companies = Company.objects.filter(num_employees__gte=form.cleaned_data.get('num_employees'))

    return render(request, 'data/company.html', {'form': form, 'companies': companies})
