from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length = 255)
    data = models.ImageField(blank = False, null = False)
    
    def __str__(self):
        return self.name

class File_Upload(models.Model):
    data = models.ImageField(blank = False, null = False, upload_to = 'images/')
    filename = models.ForeignKey('Board', related_name = 'post',\
        on_delete = models.SET_NULL, null = True, db_column = 'filename')
    
    def __str__(self):
        return self.filename