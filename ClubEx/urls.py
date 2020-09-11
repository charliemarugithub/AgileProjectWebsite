from django.urls import path

from . import views

from .views import video

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('plans/', views.plans, name='plans'),
    path('classes/', views.classes, name='classes'),
    path('videos/', video, name='videos'),
    path('contact/', views.contact, name='contact'),
    path('payment10/', views.payment10, name='payment10'),
    path('payment100/', views.payment100, name='payment100'),
    path('weekly/', views.weekly, name='weekly'),
    path('classes/yoga/', views.classes_yoga, name='classes_yoga'),
    path('classes/boxing/', views.classes_boxing, name='classes_boxing'),
    path('classes/pilates/', views.classes_pilates, name='classes_pilates'),
    path('classes/taichi/', views.classes_tai_chi, name='classes_tai_chi'),
    path('classes/aerobics/', views.classes_aerobics, name='classes_aerobics'),
    path('classes/spinning/', views.classes_spinning, name='classes_spinning'),

]
