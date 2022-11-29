from django.urls import path
from members import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('business',views.business,name='business'),
    path('contact',views.contact,name='contact')
]
