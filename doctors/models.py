from django.db import models
from django.db.models.signals import pre_save
from foodconf.models import Unit , ItemGroup , Choises,FoodTable
import os
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.conf import settings

from foodconf.models import Unit




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




sex_choises = (	("male","Male" ),
				("female","Female"))

activity = ( ('sedentary','sedentary') ,
			 ('low_activity' , 'low_activity' ) ,
			 ('active' , 'active' ) ,
			 ('very_active', 'very_active'))


class Patient(models.Model):
	"""docstring for ClassName"""

	doctor = models.ForeignKey(DoctorProfile,on_delete = models.CASCADE,blank=True,null=True)
	full_name    = models.CharField( max_length=200 )
	age    = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	weight = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	hiegth   = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	sex    = models.CharField(choices=sex_choises, max_length=200)
	phone_number = models.CharField( max_length=200 , blank=True,null=True)
	email_adress = models.EmailField(max_length =250,blank=True , null=True)
	adress_one   = models.CharField( max_length=300 ,null=True ,blank=True)
	strat_date   = models.DateField(blank=True ,null=True)
	activity = models.CharField(choices=activity, max_length=200 ,null=True,blank=True)
	calu = models.CharField( max_length=300 ,null=True ,blank=True)

	def __str__(self):
		return self.full_name 


def calculate_caloiries ( age ,wieght , height  ,sex=None ,PA = None):  

	# 3*12 > 4
	pa = 1 
	if PA == 'sedentary' :
		pa = 1

	if not PA or PA == 'low_activity' :

		pa  = 1.1
		if sex =='F':
			pa = 1.12
		return(pa)

	if PA == 'active':
		pa = 1.25
		if sex =='F':
			pa = 1.27

	if PA == 'very_active' :
		pa= 1.48
		if sex =='F':
			pa = 1.45

	
	if int(age) < 36 :
		if int(age) <= 3 :
			eer = ((89 * float(wieght)) -100) + 175
			return(eer)
		if int(age) >= 4 and int(age) <= 6 :
			eer = ((89 * float(wieght)) -100) + 156
			return(eer)
		if int(age) >= 7 and int(age) <= 12 :
			eer = ((89 * float(wieght)) -100) + 22
			return(eer)
		if int(age) >= 13 and int(age) <= 35 :
			eer = ((89 * float(wieght)) -100) + 20
			return(eer)

   
	if age in range(36 , 109) and sex=='male' :
		age = float(age)/12
		eer  = 88.5 -(61.9 * age )+pa*((26.7 * float(wieght)) +(903* float(height))) + 20 
		return(eer)
	if age in range(36 , 109) and sex=='female' :
		age = float(age)/12
		eer  = 135.3 -(30.8 * age )+pa*((10 * float(wieght)) +(934*float(height))) + 20
		return (eer )
	if age in range(109 , 217) and sex=='male' :
		age = float(age)/12
		eer  = 88.5 -(61.9 * age )+pa*((26.7 * float(wieght)) +(903*float(height))) + 25 
		return(eer)
	if age in range(109 , 217) and sex=='female' :
		age = float(age)/12
		eer  = 135.3 -(30.8 * age )+pa*((10 *float(wieght)) +(934*float(height))) + 25
		return (eer )
	if age > 217 and sex=='male' :
		age = float(age)/12
		eer = 662 -(9.53 * age )+pa*((15.91 * float(wieght)) +(539.6*float(height)))  
		return(eer)
	if age > 217 and sex=='female' :
		age = float(age)/12
		eer = 354 -(6.91 * age )+pa*((9.36 * float(wieght)) +(726*float(height)))
		return (eer )


def my_callback(sender, instance, *args, **kwargs):
	age = float(instance.age) *12

	instance.calu = calculate_caloiries(age , float(instance.weight) , float(instance.hiegth) ,instance.sex, instance.activity)
	# print(instance.calu)

pre_save.connect(my_callback, sender=Patient)

class MealsTFR(models.Model):
	patient = models.ForeignKey("Patient"  ,on_delete = models.CASCADE ,default=1)
	meals = models.ForeignKey(Unit)
	count = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)


	def __str__(self):
		return str(self.meals)

class PatientTFR(models.Model):
	id=     models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	patient = models.ForeignKey("Patient"  ,on_delete = models.CASCADE)
	meals    = models.ManyToManyField( MealsTFR ,blank=True ,null=True) 
	date_for = models.DateField(blank=True ,null=True)
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


	def __str__(self):
		return (str(self.patient) + ":"+str(self.date_for))


def my_tweentreacl(sender, instance, *args, **kwargs):
	refuse           = 0
	water            = 0
	enerygy          = 0
	protein          = 0
	fat              = 0
	ASH              = 0
	fiber            = 0
	Carbohydrate     = 0
	sodium           = 0
	potasium         = 0
	Calcium          = 0
	phorphorus       = 0
	magnisum         = 0
	iron             = 0
	zinc             = 0
	coper            = 0
	vitamen_a        = 0
	vitamen_c        = 0
	thiamen          = 0
	riboflabn     	 = 0
	if instance.id :
		for i in instance.meals.all() :
			# print (i.unit.description)
			refuse += (float(i.count) * float(i.meals.refuse))
			water += (float(i.count) *float(i.meals.water))
			enerygy += (float(i.count) *float(i.meals.enerygy))
			protein +=(float(i.count) *float(i.meals.protein))
			fat +=(float(i.count) * float(i.meals.fat))
			ASH += (float(i.count) *float(i.meals.ASH))
			fiber += (float(i.count) *float(i.meals.fiber))
			Carbohydrate += (float(i.count) * float(i.meals.Carbohydrate))
			sodium += (float(i.count) *float(i.meals.sodium))
			potasium += (float(i.count) * float(i.meals.potasium))
			Calcium += (float(i.count) *float(i.meals.Calcium))
			phorphorus += (float(i.count) * float(i.meals.phorphorus))
			magnisum += (float(i.count) *float(i.meals.magnisum))
			iron += (float(i.count) * float(i.meals.iron))
			zinc += (float(i.count) * float(i.meals.zinc))
			coper += (float(i.count) *float(i.meals.coper))
			vitamen_a+= (float(i.count) * float(i.meals.vitamen_a))
			vitamen_c += (float(i.count) *float(i.meals.vitamen_c))
			thiamen += (float(i.count) *float(i.meals.thiamen))
			riboflabn +=(float(i.count) *float(i.meals.riboflabn))

	instance.refuse = refuse
	instance.water = water
	instance.enerygy = enerygy
	instance.protein = protein
	instance.fat = fat
	instance.ASH = ASH
	instance.fiber=fiber
	instance.Carbohydrate = Carbohydrate
	instance.sodium = sodium
	instance.potasium = potasium
	instance.Calcium =Calcium
	instance.phorphorus =phorphorus
	instance.magnisum =magnisum
	instance.iron = iron
	instance.zinc =zinc
	instance.coper =coper
	instance.vitamen_c = vitamen_c
	instance.vitamen_a = vitamen_a
	instance.thiamen = thiamen
	instance.riboflabn = riboflabn

pre_save.connect(my_tweentreacl, sender=PatientTFR)