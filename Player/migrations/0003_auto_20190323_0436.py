# Generated by Django 2.1.7 on 2019-03-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='up_date',
            field=models.DateTimeField(),
        ),
    ]