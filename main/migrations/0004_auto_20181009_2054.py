# Generated by Django 2.0.6 on 2018-10-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181009_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
