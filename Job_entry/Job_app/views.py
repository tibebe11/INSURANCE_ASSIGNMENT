from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib  import messages
from .models import ContactMessage,ContactInformation,CarouselItem,Category,AboutText,Job,JobApplication,Testimonial
# Create your views here.
def testimonial(request):
   info = ContactInformation.objects.all().first()
   testimonials = Testimonial.objects.all()
  
   return render(request, 'testimonial.html',{'info':info,'testimonials': testimonials})
def home(request):
   info = ContactInformation.objects.all().first()
   categories = Category.objects.all()
   carousel_items = CarouselItem.objects.all()
   testimonials = Testimonial.objects.all()
   return render(request, 'job.html',{'carousel_items': carousel_items,'info':info,'categories': categories,'testimonials': testimonials})
def about(request):
   info = ContactInformation.objects.all().first()
   about = AboutText.objects.first() 
   return render(request, 'about.html',{'about': about,'info':info})
def catagory(request):
   info = ContactInformation.objects.all().first()
   categories = Category.objects.all()
   return render(request, 'category.html', {'categories': categories,'info':info})
def contact(request):
   info = ContactInformation.objects.all().first()
   if request.method == 'POST':
      
      name1  = request.POST.get('name')
      email1  = request.POST.get('email')
      subject1  = request.POST.get('subject')
      message1  = request.POST.get('message')
      
      contact = ContactMessage()
      
      contact.name = name1
      contact.email = email1
      contact.subject = subject1
      contact.message =message1
      
      contact.save()
         
      
      
   else:
      pass
  
   return render(request, 'contact.html',{'info':info})
def job_detail(request,job_id):

   info = ContactInformation.objects.all().first()
   job = get_object_or_404(Job, id=job_id)
   if request.method == 'POST':
        name = request.POST.get('name')
       
        email = request.POST.get('email')
        portfolio_website = request.POST.get('portfolio_website')
        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter')
        job_app = JobApplication()
        job_app.job=job
        job_app.name=name
        job_app.email=email
        job_app.portfolio_website=portfolio_website
        job_app.resume=resume
        job_app.cover_letter=cover_letter
        
        job_app.save()

       

        

   return render(request, 'jobdetail.html',{'info':info,'job': job})


def job_list(request):
   info = ContactInformation.objects.all().first()
   jobs = Job.objects.all()
   return render(request, 'joblist.html', {'jobs': jobs,'info':info})



def login(request):
   
    return render(request, 'login.html')


def signin(request):
    return render(request, 'signin.html')

def signup(request):
   if request.method == 'POST':
      fullname = request.POST['fullname']
      name = request.POST['name']
      email = request.POST['email']
      
      phone = request.POST['phone']
      password = request.POST['password']
      password2 = request.POST['password']
      
        # Check if a user with this username already exists
 
  
   return render(request, 'signup.html')

def signout(request):
    pass






