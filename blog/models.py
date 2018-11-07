from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import gettext_lazy as _
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Comment(models.Model):
    comment = models.TextField(verbose_name=_('Comment Text'))
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post) + "'s Comment"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
