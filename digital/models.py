from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    prename = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email

    