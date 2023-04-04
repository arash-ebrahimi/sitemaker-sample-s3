from django.db import models
from django.urls import reverse

class dirUploadedImages(models.Model):
    rootID = models.IntegerField(default=0)
    name = models.CharField(max_length=200, null=False)
    def __str__(self):
        return ('{} @ {} --> {}'.format(self.pk, self.name, self.rootID))

class Picture(models.Model):
    picture_addr = models.ImageField(upload_to='Images/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    dir = models.IntegerField(blank=True, null=True, default=1)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return ('{} @ {}'.format(self.pk, self.dir))

class Page(models.Model):
    name = models.CharField(max_length=200, null=False)
    section = models.CharField(max_length=200, null=False)
    contextName = models.CharField(max_length=200, null=False)
    context = models.JSONField(blank=True, null=True)

    def __str__(self):
        return ('{} @ {} - {} # {}'.format(self.pk, self.name, self.section, self.contextName))


