# Generated by Django 2.0.6 on 2018-10-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20181011_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('fos', models.CharField(max_length=200)),
                ('uni', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('date_from', models.IntegerField()),
                ('date_to', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
