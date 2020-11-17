from django.db import models


class Description(models.Model):
    job_list = (('Java Developer', 'Java Developer'), ('Sales Manager', 'Sales Manager'))
    title = models.CharField(max_length=100, null=True)
    jobs = models.CharField(max_length=100, choices=job_list, null=True)
    job_description = models.TextField(max_length=500,  null=True)

    def __str__(self):
        return self.title

