# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User




def login_page(request):
	if request.method=='POST':
		name = request.POST.get("username")
		passo = request.POST.get("password")
		user = authenticate(request ,username=name, password=passo)
		if user is not None:
       		 login(request, user)
       		
       		
       		 return redirect('/profile/{user_id}'.format(user_id = user.id) )


	return render(request ,"login.html")