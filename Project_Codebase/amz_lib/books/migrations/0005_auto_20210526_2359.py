# Generated by Django 3.1.2 on 2021-05-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_bookmark_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
