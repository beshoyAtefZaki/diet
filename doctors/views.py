# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,redirect
from .models import DoctorProfile,Patient,sex_choises,activity ,PatientTFR,MealsTFR
# Create your views here.

from django.contrib.auth.decorators import login_required

from foodconf.models import Unit,ItemGroup
from django.db.models import Q
from django.utils.timezone import datetime

@login_required(login_url='/login')
def profile_page(request):
	usr_doctor = DoctorProfile.objects.get(user = request.user)
	patient = Patient.objects.filter(doctor= usr_doctor).count()
	content = {"doctor": usr_doctor,
	"patient" :patient}
	return render(request,"profile.html" ,content)



@login_required(login_url='/login')
def get_dc_aptient(request):
	
	n_doctor = DoctorProfile.objects.get(user = request.user)
	d= Patient.objects.filter(doctor=n_doctor)
	if request.GET.get('name') :
		d=	Patient.objects.filter(doctor=n_doctor , full_name__icontains=request.GET.get('name'))

	content ={
	"doctor" : n_doctor ,
	"patient" : d
	}
	return render(request ,"patient.html" ,content)



@login_required(login_url='/login')
def patient_detail(request,patient_id ):
	n_doctor = DoctorProfile.objects.get(user = request.user)
	patient = Patient.objects.get(id=patient_id ,doctor= n_doctor)
	tfhr =   PatientTFR.objects.filter(patient= patient).last()                    
	content={
	 	"patient":patient ,
	 	"tfhr" : tfhr
 		}
	return render(request ,"p_profile.html" , content)

@login_required(login_url='/login')
def create_patient(request):
	n_doctor = DoctorProfile.objects.get(user = request.user)
	if request.method == 'POST':
		
		a =Patient( doctor     =n_doctor                       , full_name   = request.POST.get('full_name') ,
					age        =request.POST.get('age')        , weight      = request.POST.get('weight')  ,
				    hiegth     =request.POST.get('hiegth')     , sex         = request.POST.get('sex') ,
					activity   =request.POST.get('activity')   , phone_number= request.POST.get('phone_number'),
					adress_one =request.POST.get('adress_one') )
		a.save()
		return redirect('/patient_detail/{patient_id}'.format(patient_id = a.id) )

	

	content={"sex_choises" :[e[0] for e in sex_choises] ,
	"activity": [e[0] for e in activity ]}
	return render(request ,"create_pa.html" ,content)




@login_required(login_url='/login')
def create_tfhr(request , p_id=None):
	# patient = Patient.objects.get(id=p_id)
	tfhr  = PatientTFR.objects.get(id= p_id)
	patient = tfhr.patient
	units = Unit.objects.filter(item_group__isnull = False)
	item_group = ItemGroup.objects.all()
	meals = None
	r_group = None
	if (request.GET.get('group')) :
				if request.GET.get('group') != 'all':
					r_group = request.GET.get('group')
					group =  ItemGroup.objects.get(arabic_name = request.GET.get('group'))
					units = Unit.objects.filter(item_group = group)

	if (request.GET.get('search')) :
		if r_group and r_group != 'all':
			units = Unit.objects.filter( description__icontains =request.GET.get('search') ,item_group = r_group)
		else:
			units = Unit.objects.filter( description__icontains =request.GET.get('search') ,item_group__isnull = False)

	if (request.method == "POST"):
		if request.POST.get("unitid") and request.POST.get("unit_count" ) and request.POST.get('tfhr') :
			meal =tfhr.meals.create(patient=patient ,meals = Unit.objects.get(id = request.POST.get("unitid"))  ,
				count =request.POST.get("unit_count"))
			print(meal)
			meal.save()
			tfhr.save()
	meals = tfhr.meals.all()
		
	
	


	item_group = ItemGroup.objects.all()
	content ={
	"meals":meals,
	"patient":patient,
	'units':units,
	'item_group' : item_group ,
	"group":r_group,
	'tfhr':tfhr

		}

	return render(request , 'recal.html' , content)

def create_new_tfhr(request, p_id):
	patient = Patient.objects.get(id=p_id)
	tfhr = PatientTFR(patient= patient ,date_for =datetime.now() )
	tfhr.save()
	return redirect('/create-tfhr/%d'%tfhr.id)


def post_tfhr_create(request):
	if (request.method == "POST"):
		if request.POST.get("unitid") and request.POST.get("unit_count" ) and request.POST.get('tfhr') :
			meal =MealsTFR(patient=patient ,meals = Unit.objects.get(id = request.POST.get("unitid"))  ,
				count =request.POST.get("unit_count") )
			meal.save()
			tfhr = PatientTFR.objects.get(id=request.POST.get('tfhr') )
			tfhr.meals.add(meal)
			tfhr.save()
