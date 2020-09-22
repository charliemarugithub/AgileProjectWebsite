from django.shortcuts import render
from .models import Video
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


def index(request):
    return render(request, 'clubex/index.html', {'title': 'Welcome to Gym App'})


def classes(request):
    return render(request, 'clubex/classes.html', {'title': 'Classes'})


@login_required
def classes_boxing(request):
    obj = Video.objects.filter(category='Boxing')
    return render(request, 'clubex/boxing.html', {'obj': obj})


@login_required
def classes_pilates(request):
    obj = Video.objects.filter(category='Pilates')
    return render(request, 'clubex/pilates.html', {'obj': obj })


@login_required
def classes_aerobics(request):
    obj = Video.objects.filter(category='Aerobics')
    return render(request, 'clubex/aerobics.html', {'obj': obj })


@login_required
def classes_yoga(request):
    obj = Video.objects.filter(category='Yoga')
    return render(request, 'clubex/yoga.html', {'obj': obj })


@login_required
def classes_spinning(request):
    obj = Video.objects.filter(category='Spinning')
    return render(request, 'clubex/spinning.html', {'obj': obj})


@login_required
def classes_tai_chi(request):
    obj = Video.objects.filter(category='Tai Chi' or 'taichi')
    return render(request, 'clubex/taichi.html', {'obj': obj})


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


# first get the related HitCount object for your model object
hit_count = HitCount.objects.get_for_object(your_model_object)

# next, you can attempt to count a hit and get the response
# you need to pass it the request object as well
hit_count_response = HitCountMixin.hit_count(request, hit_count)

# your response could look like this:
# UpdateHitCountResponse(hit_counted=True, hit_message='Hit counted: session key')
# UpdateHitCountResponse(hit_counted=False, hit_message='Not counted: session key has active hit')