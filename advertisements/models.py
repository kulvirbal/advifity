from django.db import models
import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    gender = models.IntegerField(default=1)
    usertype = models.IntegerField(default=1)
    address = models.TextField()
    uploadedImage = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    def add_user(self):
        self.created_date = timezone.now()
        self.save()

class Types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.created_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    organization = models.CharField(max_length=255)
    hourly_rate = models.CharField(max_length=255)
    job_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    def add_post(self):
        self.created_date = timezone.now()
        self.save()

class Userpost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    resume = models.CharField(max_length=255)
    cover_letter = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    subject = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    def add_messages(self):
        self.created_date = timezone.now()
        self.save()