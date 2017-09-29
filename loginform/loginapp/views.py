from django.shortcuts import render
from.forms import loginform
from django.http import HttpResponse
def fromview(request):
	if request.session.has_key('username'):
		username=request.session['username']
		return render(request,'loggedin.html',{'username':username})
	else:
		form  = loginform()
		return render(request,'login.html',{'form':form})
def login(request):
	if request.method=='POST':
		form=loginform(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			request.session['username']=username
			return render(request,'loggedin.html',{"username":username})
		else:
			form=loginform()
			return render(request,'login.html',{'form':form})	
def logout(request):
	del request.session['username']
	return HttpResponse("<strong>you are logged out.</strong>")
# Create your views here.
