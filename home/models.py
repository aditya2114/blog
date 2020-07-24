from django.db import models

# Create your models here

class Contact(models.Model):
    srno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return 'Message from' + ' ' + self.name
