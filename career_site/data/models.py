from django.db import models


# Create your models here.
class LocationInfo(models.Model):
    id = models.IntegerField()
    address = models.CharField()
    geo_lat = models.FloatField()
    geo_alt = models.FloatField()

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'location_info'


class Company(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    num_employees = models.IntegerField()
    investment = models.IntegerField()
    revenue = models.IntegerField()
    homepage = models.CharField()
    loc_info_id = models.ForeignKey(LocationInfo, models.DO_NOTHING)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()
    class Meta:
        db_table = 'company'


class Job(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    company_id = models.ForeignKey(Company, models.DO_NOTHING)
    work_type = models.CharField()
    due_datetime = models.DateTimeField()
    min_wage = models.IntegerField()
    max_wage = models.IntegerField()
    min_experience = models.IntegerField()
    max_experience = models.IntegerField()
    loc_info_id = models.ForeignKey(LocationInfo, models.DO_NOTHING)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'job'


class Position(models.Model):
    id = models.IntegerField()
    name = models.CharField()

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'position'


class Welfare(models.Model):
    id = models.IntegerField()
    name = models.CharField()

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'welfare'


class TechStack(models.Model):
    id = models.IntegerField()
    name = models.CharField()

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'tech_stack'


class JobPositionMapping(models.Model):
    id = models.IntegerField()
    job_id = models.ForeignKey(Job, models.DO_NOTHING)
    position_id = models.ForeignKey(Position, models.DO_NOTHING)

    class Meta:
        db_table = 'job_position_mapping'


class JobTechMapping(models.Model):
    id = models.IntegerField()
    job_id = models.ForeignKey(Job, models.DO_NOTHING)
    tech_id = models.ForeignKey(TechStack, models.DO_NOTHING)

    class Meta:
        db_table = 'job_tech_mapping'


class CompanyTechMapping(models.Model):
    id = models.IntegerField()
    company_id = models.ForeignKey(Company, models.DO_NOTHING)
    tech_id = models.ForeignKey(TechStack, models.DO_NOTHING)

    class Meta:
        db_table = 'company_tech_mapping'


class CompanyWelfareMapping(models.Model):
    id = models.IntegerField()
    company_id = models.ForeignKey(Company, models.DO_NOTHING)
    welfare_id = models.ForeignKey(Welfare, models.DO_NOTHING)

    class Meta:
        db_table = 'company_welfare_mapping'
