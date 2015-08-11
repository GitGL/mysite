from django.db import models

# Create your models here.

class Areas(models.Model):
    area_name = models.CharField(max_length=100)
    area_desc = models.CharField(max_length=200)
    def __unicode__(self):
        return self.area_name

class Employees(models.Model):
    employee_id = models.CharField(max_length=8)
    employee_name = models.CharField(max_length=50)
    employee_pwd = models.CharField(max_length=200)
    def __unicode__(self):
        return self.employee_id + ": " + self.employee_name

class TimeList(models.Model):
    list_name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.list_name

class ApplyInfos(models.Model):
    area_id = models.ForeignKey(Areas)
    employee_id = models.ForeignKey(Employees)
    apply_name = models.CharField(max_length=100)
    apply_date = models.DateTimeField('date apply')
    play_date = models.DateField('date play')
    play_time = models.ForeignKey(TimeList)
    file_path = models.CharField(max_length=300)
    apply_stage = models.IntegerField(default=0)
    def __unicode__(self):
        return self.apply_name + str(self.play_date) + str(self.play_time)
