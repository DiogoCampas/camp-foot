from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

class Profile(models.Model):  #Profile class - all users of the app
    class Meta:
        db_table = 'profile'

    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name="profile")
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    position = models.TextField(max_length=200, null=True, blank=True, default="bio")
    club = models.TextField(max_length=200, null=True, blank=True, default="bio")

    # saves a profile
    def save_profile(self):     
        self.save()

    
    # deletes a profile
    def delete_profile(self):   
        self.delete()

    # user follows another user
    def follow_user(self, follower):
        return self.following.add(follower)

    # user unfllows another user
    def unfollow_user(self, to_unfollow):
        return self.following.remove(to_unfollow)

    # check if user follows a certain user
    def is_following(self, checkuser):
        return checkuser in self.following.all()

    # retrieve the number of followers of a certain user
    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    # retrieve the number of users that a certain user follows
    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    
    







