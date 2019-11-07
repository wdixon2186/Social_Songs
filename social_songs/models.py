from django.db import models

class Director(models.Model):
    films = models.TextField()
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    thumb = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)