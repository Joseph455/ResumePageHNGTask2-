from logging import fatal
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    source_url = models.URLField(max_length=500, null=False, blank=False)
    demo_url = models.URLField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    writer_name = models.CharField(max_length=200, default="Anonymous", blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.project}_{self.id}"


class Skill(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    icon = models.ImageField(upload_to="icons/", null=True)
    icon_url = models.URLField(max_length=1000, null=True, blank=True)

    
    def __str__(self) -> str:
        return self.title


