from first_app.fun_upload import handle_uploaded_file  #file upload
from .models import User   #Table creation
from .models import Signup
from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):  
   template = loader.get_template('index.html') # getting our template  
   return HttpResponse(template.render())       # rendering the template in HttpResponse  
@csrf_exempt
#print(request.POST.get('email'))#print('dict name value:',form_data['uname'])
def home(request):
	form_data=request.POST
	if request.method == 'POST':
		if request.POST.get('uname') and request.POST.get('email'):
			post=User()
			post.uname= request.POST.get('uname')
			post.email= request.POST.get('email')
			post.file=request.FILES['myfile'].name
			post.save()	
			handle_uploaded_file(request.FILES['myfile'])  
		return render(request, 'demo.html', {'total': form_data})
@csrf_exempt
def view_database(request):
	mailid= request.session['semail'] #from user table mail
	for p in User.objects.raw('SELECT * FROM first_app_user where email=%s',[mailid]):
		print(p.uname,p.email)
	return render(request, 'result.html',{'row': p})

@csrf_exempt
def signup(request): 	
	return render(request, 'signup.html') 
@csrf_exempt
def sign_insert(request):	
	if request.method == 'POST':
		post=Signup()
		post.fname=request.POST.get('firstname')
		post.lname=request.POST.get('lastname')
		post.gender=request.POST.get('gender')
		post.email=request.POST.get('email')
		post.password=request.POST.get('psw')
		post.image=request.FILES['pfile'].name
		post.save()	 
		request.session['semail'] =request.POST.get('email')
		print(request.FILES['pfile'].name)
		return render(request, 'demo.html') 
