# Generated by Django 4.2.1 on 2023-07-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0005_remove_course_content_coursecontent_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='content',
        ),
    ]
