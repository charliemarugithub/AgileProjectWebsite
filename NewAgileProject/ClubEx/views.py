from django.shortcuts import render
from .models import Video


def index(request):
    return render(request, 'index.html', {'title': 'Welcome to Gym App'})


def classes(request):
    return render(request, 'classes.html', {'title': 'Classes'})


def classes_boxing(request):
    return render(request, 'boxing.html', {'title': 'Boxing'})


def classes_pilates(request):
    return render(request, 'pilates.html', {'title': 'Pilates'})


def classes_aerobics(request):
    return render(request, 'aerobics.html', {'title': 'Aerobics'})


def classes_yoga(request):
    return render(request, 'yoga.html', {'title': 'Yoga'})


def classes_spinning(request):
    return render(request, 'spinning.html', {'title': 'Spinning'})


def classes_tai_chi(request):
    return render(request, 'taichi.html', {'title': 'Tai Chi'})


def plans(request):
    return render(request, 'plans.html',  {'title': 'Plans'})


def contact(request):
    return render(request, 'contact.html',  {'title': 'Contacts'})


def about(request):
    return render(request, 'about.html', {'title': 'About Us'})


def video(request):
    obj = Video.objects.all()
    return render(request, 'videos.html', {'obj': obj})
