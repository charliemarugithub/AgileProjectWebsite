from django.shortcuts import render
from .models import Video


def index(request):
    return render(request, 'clubex/index.html', {'title': 'Welcome to Gym App'})


def classes(request):
    return render(request, 'clubex/classes.html', {'title': 'Classes'})


def classes_boxing(request):
    return render(request, 'clubex/boxing.html', {'title': 'Boxing'})


def classes_pilates(request):
    return render(request, 'clubex/pilates.html', {'title': 'Pilates'})


def classes_aerobics(request):
    return render(request, 'clubex/aerobics.html', {'title': 'Aerobics'})


def classes_yoga(request):
    return render(request, 'clubex/yoga.html', {'title': 'Yoga'})


def classes_spinning(request):
    return render(request, 'clubex/spinning.html', {'title': 'Spinning'})


def classes_tai_chi(request):
    return render(request, 'clubex/taichi.html', {'title': 'Tai Chi'})


def plans(request):
    return render(request, 'clubex/plans.html',  {'title': 'Plans'})


def contact(request):
    return render(request, 'clubex/contact.html',  {'title': 'Contacts'})


def about(request):
    return render(request, 'clubex/about.html',  {'title': 'About Us'})


def video(request):
    obj = Video.objects.all()
    return render(request, 'clubex/videos.html', {'obj': obj})
