from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .serializers import JobSerializer
from .forms import *
from .models import *


# Create your views here.

def company(request):
    form = CompanyForm()
    companies = None

    if form.is_valid():
        companies = Company.objects.filter(num_employees__gte=form.cleaned_data.get('num_employees'))

    return render(request, 'data/company.html', {'form': form, 'companies': companies})


def job_search(request):
    form = JobSearchForm()
    return render(request, 'data/job.html', {'form': form})


def job_search_api(request):
    form = JobSearchForm(request.POST)
    if form.is_valid():
        position = form.cleaned_data['position']
        min_experience = form.cleaned_data['min_experience']
        min_wage = form.cleaned_data['min_wage']

        target_position = get_object_or_404(Position, pk=position.id)
        job_position_mapping = JobPositionMapping.objects.filter(position_id=target_position.id)
        jobs = Job.objects.filter(id__in=[mapping.job_id.id for mapping in job_position_mapping],
                                  min_wage__gte=min_wage,
                                  min_experience__gte=min_experience)

        job_serializer = JobSerializer(jobs, many=True)
        json_response = JsonResponse(job_serializer.data, safe=False)

        return json_response



        # JSON 파일로 디스크에 저장
        # serialized_data = job_serializer.data
        # with open('PATH/refined_job_api.json', 'w', encoding='utf-8') as f:
        #     json.dump(serialized_data, f, ensure_ascii=False, indent=4)

        # return JsonResponse(serialized_data, safe=False)
