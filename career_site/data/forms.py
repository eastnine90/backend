from django import forms
from .models import Company, Job, Position


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['num_employees', 'investment', 'revenue']


class JobForm(forms.ModelForm):
    min_experience_choice = [(i, f"{i}년 이상") if i > 0 else (i, "신입") for i in range(10)]
    min_experience = forms.ChoiceField(choices=min_experience_choice, label='경력')

    min_wage_choice = [(i * 1000, f"{str(i)[0]},{str(i)[1:]} 이상") for i in range(3000, 8000 + 1, 500)]
    min_wage = forms.ChoiceField(choices=min_wage_choice, label='연봉')

    class Meta:
        model = Job
        fields = ['min_experience', 'min_wage']


class PositionForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Position.objects.values_list('name'), label='직무')

    class Meta:
        model = Position
        fields = ['name']
