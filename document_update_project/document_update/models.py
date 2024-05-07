# models.py
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
