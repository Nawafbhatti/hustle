# Generated by Django 4.1.6 on 2023-02-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('cell', models.CharField(max_length=255)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(related_name='speaker', to='app.speaker'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(related_name='sponsor', to='app.sponsor'),
        ),
    ]