from django.db import models

# Create your models here.
# portfolio/models.py
from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=200, default="John Paolo A. Silvano")
    title = models.CharField(max_length=200, default="Junior Python/Django Developer")
    email = models.EmailField(default="johnpaolosilvano24@gmail.com")
    github = models.CharField(max_length=200, blank=True, default="github.com/Johnz010823")
    linkedin = models.CharField(max_length=200, blank=True, default="John Paolo Silvano")
    short_intro = models.TextField(
        default="I am a Junior Developer who enjoys converting ideas into functional applications using Python, Django, HTML/CSS, and JavaScript.")

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    role = models.CharField(max_length=200, blank=True)
    tech_stack = models.CharField(max_length=300, blank=True)
    features = models.TextField(blank=True, help_text="Comma or newline separated features.")
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    screenshot = models.ImageField(upload_to='project_screens/')

    order = models.IntegerField(default=0, help_text="Lower number appears first.")

    def feature_list(self):
        # return list of features
        return [f.strip() for f in self.features.splitlines() if f.strip()] or [f.strip() for f in
                                                                                self.features.split(',') if f.strip()]

    def __str__(self):
        return self.title

