# Generated by Django 4.2.6 on 2023-10-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_delete_seatingcapacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('reserved_id', models.AutoField(primary_key=True, serialize=False)),
                ('reference_number', models.CharField(max_length=10)),
                ('area_id', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('user_id', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
