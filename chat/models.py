from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Room(models.Model):
    name = models.CharField(verbose_name='Room Name', max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


# class MessageStatus(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     content = models.ForeignKey(Message, on_delete=models.CASCADE)
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return self.id
