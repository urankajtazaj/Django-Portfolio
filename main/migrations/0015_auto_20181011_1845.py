# Generated by Django 2.0.6 on 2018-10-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]