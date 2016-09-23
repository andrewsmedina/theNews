from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

import datetime

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255,
                             unique_for_date='pub_date')
    slug = models.CharField(max_length=255,
                            blank=True, null=True)
    body = models.TextField()
    pub_date = models.DateField(default=datetime.date.today)
    updated_date = models.DateField(default=datetime.date.today)
    tags = models.ManyToManyField(Tag)
    promoted = models.BooleanField(default=False)
    author = models.ForeignKey(User,
                               null=True,
                               blank=True,
                               default=None,
                               on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug,
                                                 'year': self.pub_date.strftime("%Y"),
                                                 'month': self.pub_date.strftime("%b"),
                                                 'day': self.pub_date.strftime("%d")}
                       )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']



