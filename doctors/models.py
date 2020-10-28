from django.db import models
from django.db.models.signals import pre_save

from foodconf.models import Unit , ItemGroup , Choises,FoodTable

import os
# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.conf import settings






class DoctorProfile (models.Model):
	user         = models.ForeignKey(User , on_delete=models.CASCADE )
	full_name    = models.CharField( max_length=200 )
	phone_number = models.CharField( max_length=200 )
	email_adress = models.EmailField(max_length =250)
	image        = models.ImageField(upload_to="media")
	password     =  models.CharField( max_length=200 ,null=True)
	adress_one   = models.CharField( max_length=300 ,null=True)
	adress_tow   = models.CharField( max_length=300 ,null=True)
	birthday     = models.DateField()
	strat_date   = models.DateField(default=datetime.now())
	end_date     = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.full_name
	







class MsureUnit(models.Model):
	item                = models.ForeignKey(FoodTable , on_delete=models.CASCADE ,null=True , blank=True)
	unit                = models.ForeignKey(Unit , on_delete=models.CASCADE ,null=True ,blank=True)
	count              	= models.DecimalField(max_digits=10, decimal_places=2 ,blank=True , null=True ,default =1)
	wieght              = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True , null=True)
	def __str__(self) :
		wght = str(self.wieght) + " "+"GM"
		if self.item :
			name = self.item.item_arabic_name
			wght = str(self.wieght) + " "+"GM"
		if self.unit :
			name = self.unit.description
			wght = str(self.unit.home_standrd_wieght * self.count) + " "+"GM"
		return  wght+ " " + name
class FoodMix(models.Model):
	description = models.CharField( max_length=200 ,blank=True , null=True)
	home_standrd        = models.CharField( max_length=200 ,blank=True , null=True)
	home_standrd_wieght = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True , null=True)
	ingredients         = models.ManyToManyField(MsureUnit)
	item_group          = models.ForeignKey(ItemGroup , on_delete=models.CASCADE ,null=True,blank=True)
	standard_unit_count = models.DecimalField(max_digits=10, decimal_places=2,default=1 ,null=True)
	standard_unit    = models.ForeignKey(Choises , on_delete=models.CASCADE ,null=True ,blank=True)
	refuse           = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	water            = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	enerygy          = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	protein          = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	fat              = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	ASH              = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True , null=True)
	fiber            = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	Carbohydrate     = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	sodium           = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	potasium         = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	Calcium          = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	phorphorus       = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	magnisum         = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	iron             = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	zinc             = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	coper            = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	vitamen_a        = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	vitamen_c        = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	thiamen          = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	riboflabn        = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)







