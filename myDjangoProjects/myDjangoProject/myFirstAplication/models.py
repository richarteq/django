from django.db import models

# Create your models here.

from django.db.models.constraints import UniqueConstraint

class Organization(models.Model):    
    name = models.CharField(unique=True, max_length=150, null=False, blank=False)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=100, null=False, blank=False)
    website = models.URLField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, null=False, auto_now=True)
    
    def __str__(self):
        return "%s %s %s %s" % (self.name, self.email, self.status, self.created)
