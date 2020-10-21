from django.db import models

# Create your models here.

class Documents(models.Model):
    document = models.FileField(upload_to='uploads/')



class e2k(models.Model):
    e2k_file = models.FileField(upload_to='uploads/')