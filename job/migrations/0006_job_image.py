# Generated by Django 3.0.7 on 2020-06-25 20:04

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to=job.models.image_upload),
            preserve_default=False,
        ),
    ]
