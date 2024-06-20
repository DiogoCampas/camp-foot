from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models import Q
# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    club = models.CharField(max_length=200)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def follow_user(self, follower):
        return self.following.add(follower)

    def unfollow_user(self, to_unfollow):
        return self.following.remove(to_unfollow)

    def is_following(self, checkuser):
        return checkuser in self.following.all()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

  


class Publication(models.Model):
    title = models.CharField(max_length=5000)
    content = models.TextField()
    author = models.ForeignKey(Record, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save_publication(self):
        self.save()
    
    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pictures = cls.objects.get(pk=id)
        return pictures
    
    @classmethod
    def search_image(cls, search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls, id):
        pictures=cls.objects.filter(id=id).update(id=id)
        return pictures

    @classmethod
    def update_description(cls, id):
        pictures = cls.objects.filter(id=id).update(id=id)
        return pictures









    
    







