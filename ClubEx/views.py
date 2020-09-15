from django.shortcuts import render
from .models import Video
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    return render(request, 'clubex/index.html', {'title': 'Welcome to Gym App'})


@login_required
def classes(request):
    return render(request, 'clubex/classes.html', {'title': 'Classes'})


@login_required
def classes_boxing(request):
    return render(request, 'clubex/boxing.html', {'title': 'Boxing'})


@login_required
def classes_pilates(request):
    return render(request, 'clubex/pilates.html', {'title': 'Pilates'})


@login_required
def classes_aerobics(request):
    return render(request, 'clubex/aerobics.html', {'title': 'Aerobics'})


@login_required
def classes_yoga(request):
    return render(request, 'clubex/yoga.html', {'title': 'Yoga'})


@login_required
def classes_spinning(request):
    return render(request, 'clubex/spinning.html', {'title': 'Spinning'})


@login_required
def classes_tai_chi(request):
    return render(request, 'clubex/taichi.html', {'title': 'Tai Chi'})


@login_required
def plans(request):
    return render(request, 'clubex/plans.html',  {'title': 'Plans'})


def contact(request):
    return render(request, 'clubex/contact.html',  {'title': 'Contacts'})


def about(request):
    return render(request, 'clubex/about.html',  {'title': 'About Us'})


@login_required
def video(request):
    query = request.GET.get('q')
    results = Video.objects.filter(
        Q(category__icontains=query) |
        Q(video_name__icontains=query) |
        Q(content__icontains=query)
    )
    return render(request, 'clubex/videos.html', {'results': results})

