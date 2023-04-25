from django.contrib.auth import get_user_model
from django.db import models
from tinymce import models as tinumce_models

User = model = get_user_model()


class Quote(models.Model):
    languages = (
        ("EN", "English"),
        ("PL", "Polish"),
    )

    approve_choices = (
        ("AP", "Approved"),
        ("WT", "Waiting"),
        ("RJ", "Rejected"),
    )

    title = models.CharField(max_length=50, unique=True, blank=True)
    content = tinumce_models.HTMLField(max_length=2000, unique=True, blank=True)
    author = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=2, choices=languages, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    favorites = models.ManyToManyField(User, related_name="favorite_quotes", blank=True)
    public = models.BooleanField(default=False)
    approved = models.CharField(max_length=2, choices=approve_choices, default="WT")

    def __str__(self) -> str:
        return self.title
