# Generated by Django 3.2.3 on 2021-05-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210526_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
