# Generated by Django 3.1.1 on 2020-11-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='job_description',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='description',
            name='jobs',
            field=models.CharField(choices=[('Java Developer', 'Java Developer'), ('Sales Manager', 'Sales Manager')], max_length=100, null=True),
        ),
    ]