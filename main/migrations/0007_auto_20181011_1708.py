# Generated by Django 2.0.6 on 2018-10-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181010_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.RemoveField(
            model_name='project',
            name='picture',
        ),
        migrations.AddField(
            model_name='project',
            name='short_desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tech',
            field=models.CharField(choices=[(1, 'Java'), (2, 'Python'), (3, 'PHP'), (4, 'JavaScript')], default=1, max_length=30),
        ),
    ]
