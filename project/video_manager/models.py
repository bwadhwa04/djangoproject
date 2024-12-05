from django.db import models
from authentication.models import User
from django.conf import settings
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField()
    video_file = models.FileField(upload_to='media/videos/') 
    thumbnail = models.ImageField(upload_to='media/thumbnails/') 
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_like_count(self):
        return self.likes.filter(value=True).count()

    def get_dislike_count(self):
        return self.likes.filter(value=False).count()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class LikesDislikes(models.Model):
    video = models.ForeignKey(Video,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BooleanField()

    class Meta:
        unique_together = ('video', 'user')
