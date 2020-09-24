from django.urls import path

from . import views

from .views import video


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('plans/', views.plans, name='plans'),
    path('classes/', views.classes, name='classes'),
    path('videos/', video, name='videos'),
    path('stats/', views.stats, name='stats'),
    path('<int:id>', views.video_details, name='video_details'),
    path('contact/', views.contact, name='contact'),
    path('classes/yoga/', views.classes_yoga, name='classes_yoga'),
    path('<int:id>', views.classes_yoga_details, name='video_details'),
    path('classes/boxing/', views.classes_boxing, name='classes_boxing'),
    path('<int:id>', views.classes_boxing_details, name='video_details'),
    path('classes/pilates/', views.classes_pilates, name='classes_pilates'),
    path('<int:id>', views.classes_pilates_details, name='video_details'),
    path('classes/taichi/', views.classes_tai_chi, name='classes_tai_chi'),
    path('<int:id>', views.classes_taichi_details, name='video_details'),
    path('classes/aerobics/', views.classes_aerobics, name='classes_aerobics'),
    path('<int:id>', views.classes_aerobics_details, name='video_details'),
    path('classes/spinning/', views.classes_spinning, name='classes_spinning'),
    path('<int:id>', views.classes_taichi_details, name='video_details'),
    
 
]
