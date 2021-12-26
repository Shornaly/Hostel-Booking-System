# Generated by Django 4.0 on 2021-12-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_roommodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=17)),
                ('email', models.CharField(max_length=17)),
                ('category', models.CharField(max_length=17)),
            ],
        ),
    ]
