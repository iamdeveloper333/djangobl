# Generated by Django 2.1.2 on 2019-01-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_remove_post_job_like_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_description',
            field=models.TextField(default=None, null=True),
        ),
    ]
