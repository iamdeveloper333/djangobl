# Generated by Django 2.1.1 on 2018-10-02 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20181002_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]