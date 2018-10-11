from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    profesion = models.TextField(max_length=300, null=True, blank=True)
    exerpt = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    fos = models.CharField(max_length=200)
    uni = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_from = models.IntegerField()
    date_to = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.degree + ' - ' + self.fos


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name


class Project(models.Model):

    TECH = (
        ('Java', "Java"),
        ('Python', "Python"),
        ('PHP', "PHP"),
        ('JS', "JavaScript"),
    )

    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=350)
    tech = models.CharField(max_length=30, choices=TECH, default=1)


    def __str__(self):
        return self.name + ' - ' + self.tech