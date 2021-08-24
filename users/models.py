from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE) #firstname, secondname, username, email, password, datejoined
    image = models.ImageField(default='user.png', blank=True)
    gender = models.CharField(max_length=50, default='None')
    intro = models.CharField(max_length=150)