from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=269)
    last_name = models.CharField(max_length=269)
    designation = models.CharField(max_length=269)
    photo = models.ImageField(upload_to="photots/%Y/%m/%d")
    facebook_link = models.CharField(max_length=270)
    twitter_link = models.CharField(max_length=270)
    instagram_link = models.CharField(max_length=270)
    createed_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name