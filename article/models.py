from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    pub_date = models.DateField(auto_created=True)
    updated_date = models.DateField(auto_now=True)

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