# Generated by Django 4.2.7 on 2023-11-28 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_choices_choice2_choices_choice3_choices_choice4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='div_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]