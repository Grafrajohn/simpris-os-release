from __future__ import unicode_literals

from django.db import models

class DocumentFile(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')