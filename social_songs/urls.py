from django.urls import path
from . import views

urlpatterns = [
    path('', views.director_list, name='director_list'),

    path('directors/<int:pk>', views.director_detail, name="director_detail"),

    path('directors/new', views.director_create, name='director_create'),


    path('directors/<int:pk>/edit', views.director_edit, name="director_edit"),

    path('directors/<int:pk>/delete', views.director_delete, name="director_delete"),

    path('video', views.showvideo, name='showvideo'),

    path('videos/<int:pk>', views.video_detail, name="video_detail"),

    path('videos/new', views.video_create, name='video_create'),

    path('videos/<int:pk>/edit', views.video_edit, name="video_edit"),

    path('videos/<int:pk>/delete', views.video_delete, name="video_delete"),
]
