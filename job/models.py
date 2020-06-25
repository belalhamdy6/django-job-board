from django.db import models
from django.utils.text import slugify

# Create your models here.
JOB_TYPE = (
    ("Full Time", "full Time"),
    ("Part Time", "part Time"),
)

def image_upload(instance, filename):
    imageNmae , extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extention)
class Job(models.Model):
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    descreption_job = models.TextField(max_length=1000)
    published_job = models.DateTimeField(auto_now=True)
    vacancy_job = models.IntegerField(default=1)
    salary_job = models.IntegerField(default=0)
    experiance_job = models.IntegerField(default=1)
    Category_job = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name