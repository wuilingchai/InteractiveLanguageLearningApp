# Generated by Django 4.2.6 on 2023-10-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='choice2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='choices',
            name='choice3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='choices',
            name='choice4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='choices',
            name='choice1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]