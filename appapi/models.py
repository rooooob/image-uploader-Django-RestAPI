from django.db import models


class Image(models.Model):
    file = models.FileField(blank=False, null=False)

    def get_image_url(self):
        return self.file.url

    def __str__(self):
        return self.file.name
