# Generated by Django 2.1rc1 on 2018-07-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20180722_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='subject_mcq',
            field=models.FloatField(blank=True, null=True, verbose_name='MCQ'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject_practical',
            field=models.FloatField(blank=True, null=True, verbose_name='Practical'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject_theory',
            field=models.FloatField(blank=True, null=True, verbose_name='Theory'),
        ),
    ]
