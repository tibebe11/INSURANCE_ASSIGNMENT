from django.contrib import admin
from .models import ContactInformation, ContactMessage,CarouselItem,Category,AboutText,Job,JobApplication,Testimonial
# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(ContactInformation)
admin.site.register(CarouselItem)
admin.site.register(Category)
admin.site.register(AboutText)
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Testimonial)
