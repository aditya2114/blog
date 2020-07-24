from django.db import models
from django.db.models import fields
import datetime

class pythonproject(models.Model):
    srno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=300)
    desc = models.TextField()
    slug = models.CharField(default="test", max_length=100)
    code = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return 'Post of' + ' '+self.Name

class webdevproject(models.Model):
    srno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=300)
    desc = models.TextField()
    slug = models.CharField(default="test", max_length=100)
    code = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return 'Post of' + ' '+self.Name

class mlproject(models.Model):
    srno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=300)
    desc = models.TextField()
    slug = models.CharField(max_length=100, default="test")
    code = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return 'Post of' + ' '+self.Name