# Generated by Django 2.1rc1 on 2018-07-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20180723_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stdsubject',
            name='subject_full_marks',
            field=models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5, null=True, verbose_name='Full Marks'),
        ),
    ]
