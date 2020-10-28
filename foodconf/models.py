from django.db import models
from django.db.models.signals import pre_save
# Create your models here.



class FoodGroup(models.Model):
	Name = models.CharField( max_length=200 ,blank=True , null=True)
	Arabic_name = models.CharField( max_length=200 ,blank=True , null=True)

	def __str__(self):
		return self.Name

class FoodTable(models.Model):


	item_name        = models.CharField( max_length=200 ,blank=True , null=True)
	item_arabic_name = models.CharField( max_length=200,blank=True , null=True)
	the_ingredients  = models.TextField(blank=True )
	item_group       = models.ForeignKey('FoodGroup' , on_delete=models.CASCADE ,null=True)
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
		return self.item_arabic_name




class HomeStandard(models.Model):
	unit_name        = models.CharField( max_length=200 ,blank=True , null=True)
	unit_arabic_name = models.CharField( max_length=200 ,blank=True , null=True)
	unit_weight      = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)




	def __str__(self):
		return self.unit_arabic_name

class Choises (models.Model) :
	arabic_name  = models.CharField( max_length=200 ,blank=True , null=True)
	english_name  = models.CharField( max_length=200 ,blank=True , null=True)
	number_of_home_unit = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
	def __str__(self) :
		return self.arabic_name

class ItemGroup(models.Model):
	arabic_name  = models.CharField( max_length=200 ,blank=True , null=True)
	english_name  = models.CharField( max_length=200 ,blank=True , null=True)
	def __str__(self):
		return self.arabic_name


class Meals (models.Model) :
	meal_name = models.CharField( max_length=1000 ,blank=True , null=True)
	def __str__(self):
		return self.meal_name

class Unit(models.Model) :
	description = models.CharField( max_length=200 ,blank=True , null=True)
	item                = models.ForeignKey('FoodTable' , on_delete=models.CASCADE ,null=True)
	home_standrd        = models.CharField( max_length=200 ,blank=True , null=True)
	home_standrd_wieght = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True , null=True)
	ingredients         = models.CharField( max_length=1000 ,blank=True , null=True)
	item_group          = models.ForeignKey('ItemGroup' , on_delete=models.CASCADE ,null=True,blank=True)
	standard_unit_count = models.DecimalField(max_digits=10, decimal_places=2,default=1 ,null=True)
	standard_unit    = models.ForeignKey('Choises' , on_delete=models.CASCADE ,null=True ,blank=True)
	meals            = models.ManyToManyField(Meals)
	avaliable        = models.DecimalField(max_digits=10, decimal_places=2,blank=True , null=True)
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

	
	def __str__(self) :
		return self.home_standrd + " "+self.description


		
# @receiver(pre_save ,sender=Unit)
def my_callback(sender, instance, *args, **kwargs):
	if instance.item and instance.standard_unit and instance.home_standrd_wieght :
		item = FoodTable.objects.get(item_arabic_name__iexact = instance.item)
		# count =  Choises.objects.get(arabic_name__iexact = instance.standard_unit)#instance.standard_unit
		weight = instance.home_standrd_wieght
		avrege = float(weight)/100
		instance.refuse           = float(item.refuse) * avrege
		instance.water            = float(item.water) *avrege
		instance.enerygy          = float(item.enerygy) *avrege
		instance.protein          = float(item.protein) *avrege
		instance.fat              = float(item.fat) *avrege
		instance.ASH              = float(item.ASH) *avrege
		instance.fiber            = float(item.fiber) *avrege
		instance.Carbohydrate     = float(item.Carbohydrate) *avrege
		instance.sodium           = float(item.sodium) *avrege
		instance.potasium         = float(item.potasium) *avrege
		instance.Calcium          = float(item.Calcium) *avrege
		instance.phorphorus       = float(item.phorphorus) *avrege
		instance.magnisum         = float(item.magnisum) *avrege
		instance.iron             = float(item.iron) *avrege
		instance.zinc             = float(item.zinc) *avrege
		instance.coper            = float(item.coper) *avrege
		instance.vitamen_a        = float(item.vitamen_a) *avrege
		instance.vitamen_c        = float(item.vitamen_c) *avrege
		instance.thiamen          = float(item.thiamen) *avrege
		instance.riboflabn        = float(item.riboflabn) *avrege

    # a =FoodTable.objects.get(item_arabic_name__iexact = instance.item)
    # print(a.enerygy)


pre_save.connect(my_callback, sender=Unit)