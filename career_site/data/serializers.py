from rest_framework import serializers
from .models import *


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = ['id', 'address', 'geo_lat', 'geo_alt']


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


class CompanySerializer(serializers.ModelSerializer):
    tech_stack = serializers.SerializerMethodField()
    welfare = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'num_employees', 'investment', 'revenue', 'homepage', 'loc_info_id', 'tech_stack',
                  'welfare']

    def get_tech_stack(self, obj):
        job_tech_mapping = CompanyTechMapping.objects.filter(company_id=obj.id)
        tech_stack = [mapping.tech_id for mapping in job_tech_mapping]
        return TechStackSerializer(tech_stack, many=True).data

    def get_welfare(self, obj):
        company_welfare_mapping = CompanyWelfareMapping.objects.filter(company_id=obj.id)
        welfare = [mapping.welfare_id for mapping in company_welfare_mapping]
        return WelfareSerializer(welfare, many=True).data


class JobSerializer(serializers.ModelSerializer):
    company_id = CompanySerializer(read_only=True)
    loc_info_id = LocationInfoSerializer(read_only=True)
    tech_stack = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id', 'name', 'company_id', 'work_type', 'due_datetime', 'min_wage', 'max_wage',
                  'min_experience', 'max_experience', 'loc_info_id', 'tech_stack', 'position']

    def get_tech_stack(self, obj):
        job_tech_mapping = JobTechMapping.objects.filter(job_id_id=obj.id)
        tech_stack = [mapping.tech_id for mapping in job_tech_mapping]
        return TechStackSerializer(tech_stack, many=True).data

    def get_position(self, obj):
        job_position_mapping = JobPositionMapping.objects.filter(job_id_id=obj.id)
        position = [mapping.position_id for mapping in job_position_mapping]
        return PositionSerializer(position, many=True).data
