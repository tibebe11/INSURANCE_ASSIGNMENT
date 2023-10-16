from django.db import models

class Insurance_Form(models.Model):
    title = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='additional_item_images')
    location = models.CharField(max_length=255)
    insurance_type = models.CharField(max_length=255)
    premium_range = models.CharField(max_length=255)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    additional_items = models.CharField(max_length=255)
    image2 = models.ImageField(upload_to='additional_item_images')

class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel')
    title = models.CharField(max_length=200)
    description = models.TextField()
    

    def __str__(self):
        return self.title
class NewsArticle(models.Model):
    image = models.ImageField(upload_to='news_images')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title