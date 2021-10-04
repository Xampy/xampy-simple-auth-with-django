from django.db import models

# Create your models here.

class Member(models.Model):
	nom = models.CharField(max_length=100,null=True)
	prenom = models.CharField(max_length=100,null=True)
	email = models.EmailField(null=False)

	password = models.CharField(max_length=100)
	validated = models.BooleanField(default=False)
