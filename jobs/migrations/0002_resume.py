# Generated by Django 4.2.1 on 2023-06-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
