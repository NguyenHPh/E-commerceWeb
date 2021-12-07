from io import BytesIO
from PIL import Image

from django.core.files import File
import uuid
from djongo import models
from django import forms

class Category(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField()

	class Meta:
		db_table = "category"
    
	def __str__(self):
		return self.name
    
	def get_absolute_url(self):
		return f'/{self.slug}/'


# class ProductDetailImages(models.Model):
# #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	image = models.ImageField(upload_to='uploads/', blank = True, null = True)
# 	thumbnail = models.ImageField(upload_to='uploads/', blank = True, null = True)

# 	class Meta:
# 		abstract = True

# class ProductDetailImagesForm(forms.ModelForm):
# 	class meta:
# 		model = ProductDetailImages
# 		fields = (
# 			'image', 'thumbnail'
# 		)

class Product(models.Model):
	id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	head_title = models.CharField(max_length=100)
	brief_component = models.TextField()
	price_before = models.DecimalField(max_digits=6, decimal_places=2)
	price_after = models.DecimalField(max_digits=6, decimal_places=2)
	lifeStage= models.CharField(max_length=50, choices=[('puppy', 'puppy'), ('adult', 'adult'), ('senior', 'senior')])
	front_image = models.ImageField(upload_to='uploads/', blank = True, null = True)
	thumbnail_front_image = models.ImageField(upload_to='uploads/', blank = True, null = True)
	# productDetailImages = models.ArrayField(
 #        model_container=ProductDetailImages,
 #        model_form_class=ProductDetailImagesForm
 #    )
	# productDetailImages = models.EmbeddedField(
	# 	model_container = ProductDetailImages,
	# )
	description = models.TextField()
	nutrition_info = models.TextField()
	deliver_info = models.TextField()
	rating = models.DecimalField(max_digits=4, decimal_places=2)

	slug = models.SlugField()


	class Meta:
		db_table = "product"

	def __str__(self):
		return self.head_title

	def get_absolute_url(self):
		return f'/{self.category.slug}/{self.slug}/'

	def get_image(self):
		if self.image:
			return 'http://127.0.0.1:8000' + self.image.url
		return ''

	def get_thumbnail(self):
		if self.thumbnail:
			return 'http://127.0.0.1:8000' + self.thumbnail.url
		else:
			if self.image:
				self.thumbnail = self.make_thumbnail(self.image)
				self.save()
				return 'http://127.0.0.1:8000' + self.image.url
			else:
				return ''

	def make_thumbnail(self, image, size = (300, 300)):
		image = Image.open(image)
		image.convert('RGB')
		img.thumbnail(size)

		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality = 300)

		thumbnail = File(thumb_io, name = image.name)

		return thumbnail
