from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio=models.CharField(max_length=700)
    designation=models.CharField(max_length=100)
    exp_year=models.IntegerField()
    email=models.EmailField(max_length=100)
    image = models.ImageField(upload_to='profile_media')
    skills = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class WorkExperience(models.Model):

    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.company_name)


class Education(models.Model):

    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    graduation_year = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.institution_name)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images')
    link = models.URLField()

    def __str__(self):
        return '{}'.format(self.title)


class Certification(models.Model):

    cer_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cer_images')
    issuing_organization = models.CharField(max_length=255)
    date_issued = models.DateField()

    def __str__(self):
        return '{}'.format(self.cer_name)