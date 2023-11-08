from django.shortcuts import render
from .forms import CompanyForm, JobForm, PositionForm
from .models import Company, Job, Position


# Create your views here.
def company(request):
    form = CompanyForm()
    companies = None

    if form.is_valid():
        companies = Company.objects.filter(num_employees__gte=form.cleaned_data.get('num_employees'))

    return render(request, 'data/company.html', {'form': form, 'companies': companies})


def job_search(request):
    job_form = JobForm()
    position_form = PositionForm()
    jobs = None

    if job_form.is_valid() and position_form.is_valid():
        name = position_form.cleaned_data['name']
        min_experience = job_form.cleaned_data['min_experience']
        min_wage = job_form.cleaned_data['min_wage']

        jobs = Position.objects.filter(name__icontains=name) & Job.objects.filter(min_experience__gte=min_experience,
                                                                                  min_wage__gte=min_wage)

    return render(request, 'data/job.html', {'job_form': job_form, 'position_form': position_form, 'jobs': jobs})
