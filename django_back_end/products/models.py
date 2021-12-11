from io import BytesIO
from PIL import Image

from django.core.files import File
import uuid
from djongo import models
# from django import forms

class Category(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to='uploads/', blank = True, null = True)
	slug = models.SlugField()

	class Meta:
		db_table = "category"
    
	def __str__(self):
		return self.name
    
	def get_absolute_url(self):
		return f'/{self.slug}'

	def get_image(self):
		if self.image:
			return 'http://127.0.0.1:8000' + self.image.url
		return 'No image'


class Product(models.Model):
	id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	special_range = models.CharField(max_length=100)
	brief_component = models.TextField()
	tray1 = models.DecimalField(max_digits=4, decimal_places=2, blank = True, null = True)
	quantity1 = models.IntegerField(blank = True, null = True)
	tray2 = models.DecimalField(max_digits=4, decimal_places=2, blank = True, null = True)
	quantity2 = models.IntegerField(blank = True, null = True)
	tray3 = models.DecimalField(max_digits=4, decimal_places=2, blank = True, null = True)
	quantity3 = models.IntegerField(blank = True, null = True)
	lifeStage= models.CharField(max_length=50, choices=[('puppy', 'puppy'), ('adult', 'adult'), ('senior', 'senior')])
	labelrange = models.CharField(max_length=50, choices=[('new', 'new'), ('small dog', 'small dog'), ('variety pack', 'variety pack'), ('national trust', 'national trust'), ('other', 'other')])
	front_image = models.ImageField(upload_to='uploads/', blank = True, null = True)
	pic1 = models.ImageField(upload_to='uploads/', blank = True, null = True)
	pic2 = models.ImageField(upload_to='uploads/', blank = True, null = True)
	pic3 = models.ImageField(upload_to='uploads/', blank = True, null = True)
	pic4 = models.ImageField(upload_to='uploads/', blank = True, null = True)
	pic5 = models.ImageField(upload_to='uploads/', blank = True, null = True)
	description = models.TextField()
	nutrition_info = models.TextField()
	feeding_guide = models.TextField()
	deliver_info = models.TextField()
	rating = models.DecimalField(max_digits=4, decimal_places=2)
	slug = models.SlugField(max_length=200, unique=True)


	class Meta:
		db_table = "product"

	def __str__(self):
		return str(self.brief_component)

	def get_absolute_url(self):
		return f'/{self.category.slug}/{self.slug}/'

	def get_image(self):
		if self.front_image:
			return 'http://127.0.0.1:8000' + self.front_image.url
		return 'no'

	def get_trays(self):
		if self.tray1:
			listTrays = []
			listTrays.append([str(self.tray1), self.quantity1])
			listTrays.append([str(self.tray2), self.quantity2])
			listTrays.append([str(self.tray3), self.quantity3])
			return listTrays
		return ''

	def get_images_detail(self):
		if self.front_image:
			listImages = []
			listImages.append('http://127.0.0.1:8000' + self.pic1.url)
			listImages.append('http://127.0.0.1:8000' + self.pic2.url)
			listImages.append('http://127.0.0.1:8000' + self.pic3.url)
			listImages.append('http://127.0.0.1:8000' + self.pic4.url)
			listImages.append('http://127.0.0.1:8000' + self.pic5.url)
			return listImages
		return ''

# class ProductDetail(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	name = models.OneToOneField(Product, on_delete=models.CASCADE)
# 	pic1 = models.ImageField(upload_to='uploads/', blank = True, null = True)
# 	pic2 = models.ImageField(upload_to='uploads/', blank = True, null = True)
# 	pic3 = models.ImageField(upload_to='uploads/', blank = True, null = True)
# 	pic4 = models.ImageField(upload_to='uploads/', blank = True, null = True)
# 	pic5 = models.ImageField(upload_to='uploads/', blank = True, null = True)
# 	description = models.TextField()
# 	nutrition_info = models.TextField()
# 	feeding_guide = models.TextField()
# 	deliver_info = models.TextField()
# 	class Meta:
# 		db_table = "productdetail"
	
# 	def __str__(self):
# 		return str(self.name.brief_component)

# 	def get_image(self):
# 		if self.front_image:
# 			listImages = []
# 			listImages.append('http://127.0.0.1:8000' + self.pic1.url)
# 			listImages.append('http://127.0.0.1:8000' + self.pic2.url)
# 			listImages.append('http://127.0.0.1:8000' + self.pic3.url)
# 			listImages.append('http://127.0.0.1:8000' + self.pic4.url)
# 			listImages.append('http://127.0.0.1:8000' + self.pic5.url)
# 			return listImages
# 		return ''

# 	def get_absolute_url(self):
# 		return f'/{self.name.category.slug}/{self.name.slug}/'