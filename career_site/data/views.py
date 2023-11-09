from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .serializers import JobSerializer, CompanySerializer
from .forms import *
from .models import *


# Create your views here.

def company(request):
    form = CompanyForm(request.POST or None)
    companies = None
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            companies = Company.objects.filter(
                num_employees__gte=form.cleaned_data.get('num_employees'),
                investment__gte=form.cleaned_data.get('investment'),
                revenue__gte=form.cleaned_data.get('revenue')
            )

            # 임시로 Json리턴하도록 설정
            if form.cleaned_data.get('get_json'):
                return JsonResponse(CompanySerializer(companies, many=True).data, safe=False,
                                    json_dumps_params={'ensure_ascii': False})

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
        json_response = JsonResponse(job_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

        return json_response

        # JSON 파일로 디스크에 저장
        # serialized_data = job_serializer.data
        # with open('PATH/refined_job_api.json', 'w', encoding='utf-8') as f:
        #     json.dump(serialized_data, f, ensure_ascii=False, indent=4)

        # return JsonResponse(serialized_data, safe=False)

def create_img(request): # 테스트 함수
    if request.method == 'POST':
        # 이곳에서 시각화 함수 처리
        pass
    test_url = "https://source.unsplash.com/user/c_v_r/1900×800"
    return JsonResponse({'image_url': test_url})

