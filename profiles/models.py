
from django.db import models
from django.contrib.auth.models import User

from blogs.models import BlogActivity

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    surname = models.CharField(max_length=50 , null=True, blank=True)
    email = models.EmailField(blank=True , null=True)
    avatar = models.FileField(default='/no_image.png' , upload_to='profiles')
    rating = models.FloatField(default=0.0)


    def change_rating(self):
        up_votes = BlogActivity.objects.filter(user=self.user).filter(activity_type='U').count()
        down_votes = BlogActivity.objects.filter(user=self.user).filter(activity_type='D').count()
        favorites = BlogActivity.objects.filter(user=self.user).filter(activity_type='F').count()
        self.rating = up_votes * 2
        print ("rating" , self.rating)
        self.save()

    def get_full_name(self):
        return '{0} {1}'.format(self.name, self.surname)

    def get_picture(self):
        return self.avatar.url

    class Meta:
        ordering = ("-rating" ,)