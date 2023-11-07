from rest_framework import serializers
from .models import *


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = ['id', 'address', 'geo_lat', 'geo_alt']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'num_employees', 'investment', 'revenue', 'homepage', 'loc_info_id']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name', 'company_id', 'work_type', 'due_datetime', 'min_wage', 'max_wage',
                  'min_experience', 'max_experience', 'loc_info_id']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class WelfareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welfare
        fields = ['id', 'name']


class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = ['id', 'name']


class JobPositionMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPositionMapping
        fields = ['id', 'job_id', 'position_id']


class JobTechMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTechMapping
        fields = ['id', 'job_id', 'tech_id']


class CompanyTechMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTechMapping
        fields = ['id', 'company_id', 'tech_id']


class CompanyWelfareMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyWelfareMapping
        fields = ['id', 'company_id', 'welfare_id']


