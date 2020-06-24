from django.db import models

# Create your models here.
JOB_TYPE = (
    ("Full Time","full Time"),
    ("Part Time","part Time"),
)


class Job(models.Model):
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    descreption_job = models.TextField(max_length=1000)
    published_job = models.DateTimeField(auto_now=True)
    vacancy_job = models.IntegerField(default=1)
    salary_job = models.IntegerField(default=0)
    experiance_job = models.IntegerField(default=1)
    def __str__(self):
        return self.title



