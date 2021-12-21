from io import BytesIO
from PIL import Image
from django.conf import settings
from django.core.files import File
import uuid
from djongo import models
from django.contrib.auth import get_user_model

User = get_user_model()


class User_Info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        db_table = "User_Info"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return 'No image'

    def __str__(self):
        return self.firstName + " " + self.lastName
