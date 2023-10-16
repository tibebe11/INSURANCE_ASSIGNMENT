from django.shortcuts import render, redirect,get_object_or_404
from Job_app.models import ContactMessage
from .models import CarouselItem
from .models import NewsArticle
from Job_app.views import carform 
from Job_app.models import CarInsurancePolicy
from django.http import HttpResponseRedirect
from Job_app.forms import CarInsurancePolicyForm
from django.shortcuts import render, redirect
from .models import Insurance_Form
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

def newsITEM(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Perform necessary validations
        if not image or not title or not description:
            error_message = "Please fill in all the fields."
            return render(request, 'newsLIST.html', {'error_message': error_message})

        # Create and save the news article
        news_article = NewsArticle(image=image, title=title, description=description)
        news_article.save()

    news_articles = NewsArticle.objects.all()
    return render(request, 'newsLIST.html', {'news_articles': news_articles})
def article_detail(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    return render(request, 'newsDetail.html', {'article': article})
def update_article(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        article.title = title
        article.description = description
        
        # Handle the uploaded image
        if 'image' in request.FILES:
            image = request.FILES['image']
            article.image = image
        
        article.save()

        return redirect('article_detail', article_id=article.id)

    return render(request, 'update_article.html', {'article': article})
def delete_article(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('article_detail')

    return render(request, 'delete_article.html', {'article': article})

def cItem(request):
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        
        carousel_item = CarouselItem(image=image, title=title, description=description)
        carousel_item.save()
        
    carousel_items = CarouselItem.objects.all()
    return render(request, 'cITEMS.html', {'carousel_items': carousel_items})
def cdetail(request, pk):
    carousel_item = get_object_or_404(CarouselItem, pk=pk)
    return render(request, 'Cdetail.html', {'carousel_item': carousel_item})

def carouselitem_update(request, pk):
    carousel_item = get_object_or_404(CarouselItem, pk=pk)
    if request.method == 'POST':
        carousel_item.title = request.POST['title']
        carousel_item.description = request.POST['description']
        if 'image' in request.FILES:
            carousel_item.image = request.FILES['image']
        carousel_item.save()
        return redirect('carouselitem_detail', pk=pk)
    return render(request, 'carouselitem_update.html', {'carousel_item': carousel_item})


def carouselitem_delete(request, pk):
    carousel_item = get_object_or_404(CarouselItem, pk=pk)
    
    if request.method == 'POST':
        carousel_item.delete()
        return redirect('citems')  # Redirect to the carousel item list page
    
    context = {'carousel_item': carousel_item}
    return render(request, 'carouselitem_delete.html', context)



def create_insurance(request):
    context = {'insure': []}  # Initialize context with an empty list
    
    if request.method == 'POST':
        title = request.POST.get('title')
        image1 = request.FILES.get('image1')
        location = request.POST.get('location')
        insurance_type = request.POST.get('insurance_type')
        premium_range = request.POST.get('premium_range')
        description = request.POST.get('description')
        responsibilities = request.POST.get('responsibilities')
        qualifications = request.POST.get('qualifications')
        additional_items = request.POST.get('additional_items')
        image2 = request.FILES.get('image2')

        # Create a new insurance instance and assign the values
        insurance = Insurance_Form(
            title=title,
            image1=image1,
            location=location,
            insurance_type=insurance_type,
            premium_range=premium_range,
            description=description,
            responsibilities=responsibilities,
            qualifications=qualifications,
            additional_items=additional_items,
            image2=image2
        )

        # Save the insurance instance to the database
        insurance.save()
    
    insure = Insurance_Form.objects.all()
    context['insure'] = insure  # Update the 'insure' key in the context
    return render(request, 'insure.html', context)


def home(request):
    
    contact_messages = ContactMessage.objects.all()
    
    
    return render(request, 'Admin.html', {'contact_messages': contact_messages})

def ADMIN_contact(request):
    return render(request, 'contactMH.html')

def delete_confirmation(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    context = {
        'message': message,
    }
    return render(request, 'delete.html', context)

def delete_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.delete()
    return redirect('home')

def insurance_list(request):
    insure = Insurance_Form.objects.all()
    return render(request, 'IL.html', {'insure': insure})

def insurance_detail(request, insurance_id):
    insurance_instance = get_object_or_404(Insurance_Form, id=insurance_id)
    return render(request, 'insuranceDetail.html', {'insurance': insurance_instance})

def insurance_update(request, insurance_id):
    insurance_instance = get_object_or_404(Insurance_Form, id=insurance_id)
    if request.method == 'POST':
        # Retrieve the updated values from the form
        insurance_instance.title = request.POST.get('title')
        insurance_instance.image1 = request.FILES.get('image1')
        insurance_instance.location = request.POST.get('location')
        insurance_instance.insurance_type = request.POST.get('insurance_type')
        insurance_instance.premium_range = request.POST.get('premium_range')
        insurance_instance.description = request.POST.get('description')
        insurance_instance.responsibilities = request.POST.get('responsibilities')
        insurance_instance.qualifications = request.POST.get('qualifications')
        insurance_instance.additional_items = request.POST.get('additional_items')
        insurance_instance.image2 = request.FILES.get('image2')
        insurance_instance.save()
        return redirect('insurance_detail', insurance_instance.id)
    return render(request, 'insuranceUpdate.html', {'insurance': insurance_instance})

def insurance_delete(request, insurance_id):
    insurance_instance = get_object_or_404(Insurance_Form, id=insurance_id)
    if request.method == 'POST':
        insurance_instance.delete()
        return redirect('insurance_list')
    return render(request, 'insurance_delete.html', {'insurance': insurance_instance})

def abc(request):
    cforms=CarInsurancePolicy.objects.all()
    return render(request,'htmlform.html',{'cforms': cforms})
def idt(request, cform_id):
    cform = get_object_or_404(CarInsurancePolicy, id=cform_id)
    return render(request, 'det.html', {'cform': cform})

def process_decision(request):
    if request.method == 'POST':
        decision = request.POST.get('decision')  # Get the decision from the POST data
        recipient_email = request.POST.get('email')  # Get the recipient email from the POST data

        # Send email notification
        if decision == 'accepted':
            subject = 'Car Insurance Policy Accepted'
            message = 'Your car insurance policy has been accepted.'
        elif decision == 'rejected':
            subject = 'Car Insurance Policy Rejected'
            message = 'Your car insurance policy has been rejected.'
        else:
            return JsonResponse({'success': False})  # Return a failure response if the decision is invalid

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        return JsonResponse({'success': True})  # Return a success response

    return JsonResponse({'success': False})  # Return a failure response for other request methods