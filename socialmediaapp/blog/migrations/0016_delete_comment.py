# Generated by Django 4.1.3 on 2022-12-07 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
