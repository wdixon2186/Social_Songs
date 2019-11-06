from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Director

from .forms import DirectorForm
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
