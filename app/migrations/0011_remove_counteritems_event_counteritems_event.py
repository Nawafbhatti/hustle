# Generated by Django 4.1.6 on 2023-02-15 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_event_counters_counteritems_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counteritems',
            name='Event',
        ),
        migrations.AddField(
            model_name='counteritems',
            name='Event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Event', to='app.event'),
        ),
    ]
