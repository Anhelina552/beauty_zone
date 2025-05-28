from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('masters/', views.master_list, name='master_list')
]


