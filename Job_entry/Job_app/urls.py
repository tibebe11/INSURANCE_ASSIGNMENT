"""
URL configuration for Job_entry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from Admin_dashboard.views import insurance_detail,insurance_list
from . import views
from news.views import blog

from .views import home,about,catagory,contact,job_detail,job_list,testimonial,carform
urlpatterns = [
   
   path('', home, name="home_url"),
   path('testimonial/', testimonial, name="testimonial"),
   path('about/', about, name="about"),
   path('catagory/', catagory, name="catagory"),
   path('contact/', contact, name="contact"),
   path('jobdetail/<int:insurance_id>/', job_detail, name="jobdetail"),
   path('joblist/', job_list, name="list"),
   path('carform/', carform, name="carform"),
   path('', blog, name="blog_url"),
  # path('login/', login, name='login'),
   ##path('logout/', logout, name='logout'),
   #path('signup/', signup, name="signup"),
 
  

]
