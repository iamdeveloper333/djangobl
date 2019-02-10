# Generated by Django 2.1.2 on 2019-01-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20190113_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField(max_length=1500)),
                ('blog_by', models.CharField(max_length=200)),
                ('blog_apply_link', models.CharField(default=None, max_length=200, null=True)),
                ('blog_img_link', models.CharField(default=None, max_length=200, null=True)),
                ('blog_created', models.DateField(blank=True, null=True)),
                ('blog_like_status', models.BooleanField(default=False)),
            ],
        ),
    ]