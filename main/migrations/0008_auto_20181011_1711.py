# Generated by Django 2.0.6 on 2018-10-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181011_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tech',
            field=models.CharField(choices=[('Java', 'Java'), ('Python', 'Python'), ('PHP', 'PHP'), ('JS', 'JavaScript')], default=1, max_length=30),
        ),
    ]
