from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50, verbose_name = 'Назва todo')
    body = models.TextField(verbose_name = 'Тіло todo')
    slug = models.SlugField(verbose_name = 'url', unique = True, blank = True)
    todo_done = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True, verbose_name='Додано')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Todo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
