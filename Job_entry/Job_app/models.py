from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ContactMessage(models.Model):
   name  = models.CharField(max_length = 200)
   email  =  models.EmailField()
   subject  = models.CharField(max_length=200)
   message = models.TextField()
   
   def __str__(self):
      return self.name+"name"
class ContactInformation(models.Model):
   
   address = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   email  = models.EmailField()
   

   def __str__(self):
      return self.email
class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel')
    title = models.CharField(max_length=200)
    description = models.TextField()
    

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=200)
    vacancy_count = models.IntegerField()
   

    def __str__(self):
        return self.name
class AboutText(models.Model):
    title = models.CharField(max_length=255)
    image_1 = models.ImageField(upload_to='about/')
    
    description_2 = models.TextField()
    description_3 = models.TextField()
    point = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='job_logos')
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=255)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    company_description = models.TextField()



    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True )
    email = models.EmailField()
    portfolio_website = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes')
    cover_letter = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.job.title}'

class Testimonial(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='testimonial_images')
    client_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name
