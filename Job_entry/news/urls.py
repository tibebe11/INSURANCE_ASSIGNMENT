from django.urls import path, include
from .views import blog,detail
urlpatterns = [
   
   path('', blog, name="blog_url"),
   path('news/<int:article_id>/', detail, name='detail'),
  
 
  

]