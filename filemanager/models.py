from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
from django import forms
import random
import string 
import pyminizip

def compressFile(filepath,password,output,):
        pyminizip.compress(f".{filepath}", None, f'{output}.zip',
                   password, 5)
        print("compressed")
class FileManageTable(models.Model):
        
        filename = models.FileField(upload_to='UploadedFiles/')
        email = models.EmailField()
        last_modified = models.DateTimeField(auto_now_add = True)
        password = models.CharField(max_length=100)
        decodekey = models.CharField(max_length=50)

        slug = models.SlugField(
                default='',
                editable=False,
                max_length=15,)

        def get_absolute_url(self):
                kwargs = {
                'pk': self.id,
                'slug': self.slug
                }
                return reverse('fileslug', kwargs=kwargs)

        def save(self, *args, **kwargs):
                value = ''.join(random.choice(string.ascii_lowercase) for i in range(15))
                self.slug = slugify(value, allow_unicode=True)
                self.decodekey = ''.join(random.choice(string.digits) for i in range(6))
                
                
                super().save(*args, **kwargs)
                print(self.filename.url)
                compressFile(self.filename.url,self.password,self.filename)
                self.filename = f"{self.filename}.zip"
                super().save(*args, **kwargs)
                def __str__(self):
                         return self.filename
        def __str__(self):
                return f"{self.slug}-{self.decodekey}"

class hashedUrl(models.Model):
        filename = models.CharField(max_length=200)
        hashkey = models.CharField(max_length=200)
        expire = models.DateTimeField(auto_now_add = True)