# Generated by Django 3.1.2 on 2021-05-20 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20210521_0303'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categories',
            new_name='AllCategories',
        ),
    ]
