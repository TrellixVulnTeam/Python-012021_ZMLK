# Generated by Django 3.2 on 2021-05-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=100)),
                ('car_typ', models.CharField(max_length=100)),
                ('km_total', models.IntegerField()),
                ('last_control', models.DateField()),
            ],
        ),
    ]
