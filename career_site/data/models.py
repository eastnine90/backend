from django.db import models


# Create your models here.
class LocationInfo(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    geo_lat = models.FloatField()
    geo_alt = models.FloatField()

    # created_at = models.DateTimeField(auto_add_now=True)
    # modified_at = models.DateTimeField(auto_add=True)

    class Meta:
        db_table = 'location_info'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    num_employees = models.IntegerField(null=True)
    investment = models.IntegerField(null=True)
    revenue = models.IntegerField(null=True)
    homepage = models.CharField(max_length=200, null=True)
    loc_info_id = models.ForeignKey(LocationInfo, models.DO_NOTHING)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()
    class Meta:
        db_table = 'company'


class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company, models.DO_NOTHING)
    work_type = models.CharField(max_length=200, null=True)
    due_datetime = models.DateTimeField(default='2999-12-31')
    min_wage = models.IntegerField(null=True)
    max_wage = models.IntegerField(null=True)
    min_experience = models.IntegerField()
    max_experience = models.IntegerField()
    loc_info_id = models.ForeignKey(LocationInfo, models.DO_NOTHING)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'job'


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'position'


class Welfare(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'welfare'


class TechStack(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # created_at = models.DateTimeField()
    # modified_at = models.DateTimeField()

    class Meta:
        db_table = 'tech_stack'


class JobPositionMapping(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, models.DO_NOTHING)
    position_id = models.ForeignKey(Position, models.DO_NOTHING)

    class Meta:
        db_table = 'job_position_mapping'


class JobTechMapping(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, models.DO_NOTHING)
    tech_id = models.ForeignKey(TechStack, models.DO_NOTHING)

    class Meta:
        db_table = 'job_tech_mapping'


class CompanyTechMapping(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, models.DO_NOTHING)
    tech_id = models.ForeignKey(TechStack, models.DO_NOTHING)

    class Meta:
        db_table = 'company_tech_mapping'


class CompanyWelfareMapping(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, models.DO_NOTHING)
    welfare_id = models.ForeignKey(Welfare, models.DO_NOTHING)

    class Meta:
        db_table = 'company_welfare_mapping'
