# Generated by Django 2.1.2 on 2019-01-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20190115_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptitudetest',
            name='category_description',
            field=models.TextField(default=None, null=True),
        ),
    ]