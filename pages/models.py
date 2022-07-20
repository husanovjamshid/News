from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RightNews(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(null=True)
    subId = models.ForeignKey(Category, related_name='subcategory', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    shorttext = models.TextField(null=True)
    text = RichTextUploadingField(null=True)
    # date = models.DateField(default=lambda : datetime.date.today() - datetime.timedelta(days=6210))
    # date = models.DateField(null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    view_count = models.IntegerField(default=0, null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title


class CenterNews(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(null=True)
    title = models.CharField(max_length=255)
    text = RichTextUploadingField(null=True)
    # date = models.DateField(default=lambda : datetime.date.today() - datetime.timedelta(days=6210))
    # date = models.DateField(null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    view_count = models.IntegerField(default=0, null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255,  blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name