from django.db import models

# Create your models here.
def get_file_path(instance, filename):
    return instance.name + '/' + filename

class Classification(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to=get_file_path)

    def __str__(self):
        return self.name