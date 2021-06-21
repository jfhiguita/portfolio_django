"""projects models module"""

from django.db import models

class Project(models.Model):
    """Projects model DB

    Args:
        models (Project): It's a model with the info for each project
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")