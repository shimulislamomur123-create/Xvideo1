
from urllib.parse import urlparse
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    website_url = models.URLField()
    category = models.CharField(max_length=100, default="Other")
    search_url = models.CharField(max_length=500, blank=True, editable=False)

    def save(self, *args, **kwargs):
        domain = urlparse(self.website_url).netloc

        if domain:
            self.search_url = (
                "https://www.google.com/search?q="
                f"site%3A{domain}+{{query}}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
