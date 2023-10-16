from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from Admin_dashboard.models import Insurance_Form
from Admin_dashboard.models import CarouselItem
from .forms import ContactForm
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CarInsurancePolicyForm
from django.contrib  import messages
from .models import ContactMessage,ContactInformation,Category,AboutText,Job,JobApplication,Testimonial,CarInsurancePolicy
from django.shortcuts import render, redirect




    


# Create your views here.

#def login(request):
#    form = Login_Form(request.POST or None)
#    if request.method == 'POST':
#        if form.is_valid():
#            email = form.cleaned_data['email']
#            password = form.cleaned_data['password']
#            user = authenticate(request, email=email,password=password)
#        if (user is not None and user.is_superuser) :
#            login(request, user)
#            return redirect('admin-dashboard')
#       
#           
#      
#        else:
#            messages.error(request, 'Invalid Password or Email')
#    context = {
#        'form' : form
#    }
#    return render(request, 'signin.html', context)
#
#
#def logout(request):
#    logout(request)
#    return render(request, 'signout.html')
#
#def signup(request):
#    form = CustomUserCreationForm(request.POST or None)
#    if request.method == 'POST':
#        if form.is_valid():
#            user = form.save(commit=False)
#            user.is_candidate = True
#            user.save()
#            messages.success(request, 'Your Account has been Successfully Created! Please Login')
#            return redirect('/login')    
#    context = {
#        'form' : form
#    }
#
#    return render(request, 'signup.html', context)
#





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
      
      form = ContactForm(request.POST)
   
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
      form = ContactForm()
         
      
      
   else:
      pass
  
   return render(request, 'contact.html',{'info':info})
def job_detail(request, insurance_id):
    insurance_instance = get_object_or_404(Insurance_Form, id=insurance_id)
    # Add any additional logic or data retrieval you need
  
    return render(request, 'jobdetail.html', {'insurance': insurance_instance})

def job_list(request):
    
    insure = Insurance_Form.objects.all()
  
    return render(request, 'joblist.html',  {'insure': insure})


def carform(request):
    if request.method == 'POST':
        insured_name = request.POST.get('insuredName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        effective_date = request.POST.get('effectiveDate')
        expiry_date = request.POST.get('expiryDate')
        vehicle_make = request.POST.get('vehicleMake')
        vehicle_model = request.POST.get('vehicleModel')
        vehicle_year = request.POST.get('vehicleYear')
        vin = request.POST.get('vin')
        driver_name = request.POST.get('driverName')
        driver_age = request.POST.get('driverAge')
        previous_status = request.POST.get('previousStatus')
        agreement = request.POST.get('agreement') == 'agree'
        
         # Get the uploaded file
        
        # Save the form data to the database
        car_insurance = CarInsurancePolicy(
            insured_name=insured_name,
            phone=phone,
            email=email,
            effective_date=effective_date,
            expiry_date=expiry_date,
            vehicle_make=vehicle_make,
            vehicle_model=vehicle_model,
            vehicle_year=vehicle_year,
            vin=vin,
            driver_name=driver_name,
            driver_age=driver_age,
            previous_status=previous_status,
            agreement=agreement,
            
        )
        car_insurance.save()
        
        messages.success(request, 'You have successfully submitted the form.')  # Success message
        
        return redirect('carform')  # Redirect back to the form page
    
    return render(request, 'forms.html')




