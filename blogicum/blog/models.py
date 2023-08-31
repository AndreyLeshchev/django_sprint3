from django.db import models
from core.models import PublishedModel
from core.models import CreatedAt
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(PublishedModel, CreatedAt):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Location(PublishedModel, CreatedAt):
    name = models.CharField(max_length=256)


class Post(PublishedModel, CreatedAt):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name ='blog',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name ='blog',
    )