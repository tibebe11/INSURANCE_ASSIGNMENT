from django.urls import path, include
from .views import home,delete_confirmation,delete_message,ADMIN_contact,create_insurance,insurance_list,insurance_delete,insurance_update,insurance_detail,abc,idt,cItem, cdetail,carouselitem_update,carouselitem_delete,newsITEM,article_detail,update_article, delete_article


urlpatterns = [
    path('', home, name="home"),
    path('contactADMIN/', ADMIN_contact, name="ContactH"),
    path('delete/confirm/<int:message_id>/', delete_confirmation, name='delete_confirmation'),
    path('delete/<int:message_id>/', delete_message, name='delete_message'),
    path('create/', create_insurance, name='create_insurance'),
    path('insure_list/', insurance_list, name='insurance_list'),
    path('insure/<int:insurance_id>/update/', insurance_update, name='insurance_update'),
    path('insure/<int:insurance_id>/delete/', insurance_delete, name='insurance_delete'),
    path('insure/<int:insurance_id>/', insurance_detail, name='insurance_detail'),
    path('policy/agreement/', abc, name='policy_agreement'),
    path('insurance_detail/<int:cform_id>/', idt, name='idt'),
    path('carosel/', cItem, name='citems'),
    path('carouselitem/<int:pk>/', cdetail, name='carouselitem_detail'),
    path('carouselitem/<int:pk>/update/',carouselitem_update, name='carouselitem_update'),
    path('carouselitem/<int:pk>/delete/', carouselitem_delete, name='carouselitem_delete'),
    path('newsITEM/', newsITEM, name='newsITEM'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('article/<int:article_id>/update/', update_article, name='update_article'),
    path('article/<int:article_id>/delete/', delete_article, name='delete_article'),
]
