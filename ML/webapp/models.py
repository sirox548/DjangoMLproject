from django.db import models
from django_pandas.managers import DataFrameManager


class Description(models.Model):
    job_list = (('Java Developer', 'Java Developer'), ('Sales Manager', 'Sales Manager'))
    title = models.CharField(max_length=100, null=True)
    jobs = models.CharField(max_length=100, choices=job_list, null=True)
    description = models.TextField(max_length=500,  null=True)

    objects = DataFrameManager()

    def __str__(self):
        return self.title

