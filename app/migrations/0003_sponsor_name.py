# Generated by Django 4.1.6 on 2023-02-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_event_speakers_event_sponsors'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
