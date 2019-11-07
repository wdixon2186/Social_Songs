from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Director, Video

from .forms import DirectorForm, VideoForm
# from django.contrib.auth.decorators import login_required


def director_list(request):
    directors = Director.objects.all()
    return render(request, 'social_songs/director_list.html', {'directors': directors})


def director_detail(request, pk):
    director = Director.objects.get(id=pk)
    return render(request, 'social_songs/director_detail.html', {'director': director})

# @login_required
def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm()
    return render(request, 'social_songs/director_form.html', {'form': form})

# @login_required
def director_edit(request, pk):
    director = Director.objects.get(pk=pk)
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm(instance=director)
    return render(request, 'social_songs/director_form.html', {'form': form})

# @login_required
def director_delete(request, pk):
    Director.objects.get(id=pk).delete()
    return redirect('director_list')


def showvideo(request):

    lastvideo= Video.objects.last()

    videofile= lastvideo.videofile

    videos = Video.objects.all()
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'videofile': videofile,
              'form': form, "videos":videos
              }
    
      
    return render(request, 'social_songs/video_list.html', context)

def video_list(request):
    videos = Video.objects.all()
    print(videos)
    return render(request, 'social_songs/video_list.html', {'videos': videos})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)  
    else:
        form = VideoForm()
    return render(request, 'social_songs/video_form.html', {'form': form})

def video_delete(request, pk):
    Video.objects.get(id=pk).delete()
    return redirect('director_list')

def video_edit(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'social_songs/video_form.html', {'form': form})

def video_detail(request, pk):
    video = Video.objects.get(id=pk)
    return render(request, 'social_songs/video_detail.html', {'video': video})