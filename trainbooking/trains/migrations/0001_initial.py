# Generated by Django 3.2.7 on 2021-09-17 05:38

from django.db import migrations, models
import trains.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('train_number', models.CharField(default=trains.models.generate_train_number, max_length=10, primary_key=True, serialize=False)),
                ('train_name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('ticket_fare', models.IntegerField(blank=True, null=True)),
                ('travel_path', models.TextField(default=list)),
            ],
            options={
                'verbose_name_plural': 'Trains',
                'ordering': ('train_number',),
            },
        ),
    ]
