from django.shortcuts import render, get_object_or_404
from .models import Video
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    return render(request, 'clubex/index.html', {'title': 'Welcome to Gym App'})


def classes(request):
    return render(request, 'clubex/classes.html', {'title': 'Classes'})


@login_required
def classes_boxing(request):
    obj = Video.objects.filter(category='Boxing')
    return render(request, 'clubex/boxing.html', {'obj': obj})


def classes_boxing_details(request, id):
    obj = get_object_or_404(Video, pk=id)
    return render(request, 'clubex/video_details.html', {'obj': obj})


@login_required
def classes_pilates(request):
    obj = Video.objects.filter(category='Pilates')
    return render(request, 'clubex/pilates.html', {'obj': obj})


def classes_pilates_details(request, id):
    obj = get_object_or_404(Video, pk=id)
    return render(request, 'clubex/video_details.html', {'obj': obj})


@login_required
def classes_aerobics(request):
    obj = Video.objects.filter(category='Aerobics')
    return render(request, 'clubex/aerobics.html', {'obj': obj})


def classes_aerobics_details(request, id):
    obj = get_object_or_404(Video, pk=id)
    return render(request, 'clubex/video_details.html', {'obj': obj})


@login_required
def classes_yoga(request):
    obj = Video.objects.filter(category='Yoga')
    return render(request, 'clubex/yoga.html', {'obj': obj})


def classes_yoga_details(request, id):
    obj = get_object_or_404(Video, pk=id)
    return render(request, 'clubex/video_details.html', {'obj': obj})


@login_required
def classes_spinning(request):
    obj = Video.objects.filter(category='Spinning')
    return render(request, 'clubex/spinning.html', {'obj': obj})


@login_required
def classes_tai_chi(request):
    obj = Video.objects.filter(category='Tai Chi' or 'taichi')
    return render(request, 'clubex/taichi.html', {'obj': obj})


def classes_taichi_details(request, id):
    obj = get_object_or_404(Video, pk=id)
    return render(request, 'clubex/video_details.html', {'obj': obj})


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


