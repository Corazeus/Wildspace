# Generated by Django 4.2.1 on 2023-10-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_delete_seatingcapacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='minutes',
            field=models.IntegerField(default=2),
        ),
    ]