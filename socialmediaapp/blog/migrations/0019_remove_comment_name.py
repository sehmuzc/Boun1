# Generated by Django 4.1.3 on 2022-12-07 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_comment_name_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
