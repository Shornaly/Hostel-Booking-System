# Generated by Django 4.0 on 2021-12-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_bookingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='room',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
    ]
