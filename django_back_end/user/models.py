from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=32)
    subcribe = models.NullBooleanField
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

        def __str__(self):
            return self.firstName + " " + self.lastName
