# Generated by Django 4.2.5 on 2023-10-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('person1', models.TextField(max_length=500)),
                ('person2', models.TextField(max_length=500)),
            ],
        ),
    ]
