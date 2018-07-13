
from django.db import models
from django.utils import timezone


class JobList(models.Model):
    url = models.CharField(max_length=4000)
    published_date = models.DateTimeField(
            blank=False, null=False)
    data = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.url
