# Generated by Django 4.2.19 on 2025-02-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sellType', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('fullAddress', models.CharField(max_length=250)),
            ],
        ),
    ]
