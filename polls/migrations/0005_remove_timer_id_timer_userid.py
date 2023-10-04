# Generated by Django 4.2.1 on 2023-10-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_timer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='id',
        ),
        migrations.AddField(
            model_name='timer',
            name='userid',
            field=models.CharField(default=1, max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
