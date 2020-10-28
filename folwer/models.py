from django.db import models

# Create your models here.
from django.conf import settings





User = settings.AUTH_USER_MODEL



sex_choises = [
				{"male":"Male" ,
				 "female":"Female"}]


class Folwer(models.Model):
	user   = models.ForeignKey(User,on_delete = models.CASCADE)
	age    = models.IntegerField()
	weight = models.IntegerField()
	tall   = models.IntegerField()
	sex    = models.CharField(choices=sex_choises, max_length=200)