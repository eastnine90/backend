from django.shortcuts import render
from rest_framework.decorators import api_view

from .forms import CompanyForm, JobForm
from .models import Company, Job


# Create your views here.
def company(request):
    form = CompanyForm()
    companies = None

    if form.is_valid():
        companies = Company.objects.filter(num_employees__gte=form.cleaned_data.get('num_employees'))

    return render(request, 'data/company.html', {'form': form, 'companies': companies})



def job_search(request):
    form = JobForm()
    jobs = None

    if form.is_valid():
        name = form.cleaned_data['name']
        min_experience = form.cleaned_data['min_experience']
        min_wage = form.cleaned_data['min_wage']

        jobs = Job.objects.filter(name__icontains=name, min_experience__gte=min_experience,
                                  min_wage__gte=min_wage)

    return render(request, 'data/job.html', {'form': form, 'jobs': jobs})
