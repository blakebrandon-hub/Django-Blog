from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	created_on = models.DateTimeField(auto_now_add=True)
	content = models.TextField(max_length=500)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return "Author: {} Post: {}".format(self.author, self.post)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(blank=True)
	bio = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return "{}'s Profile".format(self.user)
		
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    