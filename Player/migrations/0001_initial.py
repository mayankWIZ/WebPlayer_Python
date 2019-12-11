# Generated by Django 2.1.7 on 2019-03-14 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('up_date', models.DateField()),
                ('file', models.FileField(upload_to='%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('bio', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='uname',
            field=models.ForeignKey(db_column='uname', on_delete=django.db.models.deletion.CASCADE, to='Player.User'),
        ),
    ]