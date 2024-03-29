# Generated by Django 4.1.6 on 2023-03-23 10:44

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_items_use_in_home_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=256, null=True, populate_from='title', unique=True),
        ),
    ]
