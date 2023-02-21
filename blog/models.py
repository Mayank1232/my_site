from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('post_details', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
