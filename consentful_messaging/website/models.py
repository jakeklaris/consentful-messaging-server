from django.db import models
from django.db.models import IntegerField, Model
##from django_mysql.models import ListTextField

# Create your models here.

class TwitterAccount(models.Model):
  id = models.CharField(max_length = 25, primary_key=True)
  screen_name = models.TextField(blank=True, null=True)
  created_date = models.DateField(auto_now=False,auto_now_add=False,blank=True, null=True)
  follower_num = models.IntegerField(blank=True, null=True)
  following = models.ManyToManyField("self", symmetrical=False, related_name="followed",blank=True) #list of users that current user follows
  followers = models.ManyToManyField("self", symmetrical=False, related_name="follows",blank=True) #list of users that follow currentUser
  suspended = models.BooleanField(default=False,blank=True, null=True) #suspended?
  protected = models.BooleanField(blank=True, null=True) #protected?
  following_num = models.IntegerField(blank=True, null=True) # add code in tasks to retrieve following_num from api

  #code for storing list of following and followers using network_functions cursor method