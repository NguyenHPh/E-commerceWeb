# Generated by Django 3.1.12 on 2021-12-08 17:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('special_range', models.CharField(max_length=100)),
                ('brief_component', models.TextField()),
                ('tray1', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('quantity1', models.IntegerField(blank=True, null=True)),
                ('tray2', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('quantity2', models.IntegerField(blank=True, null=True)),
                ('tray3', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('quantity3', models.IntegerField(blank=True, null=True)),
                ('lifeStage', models.CharField(choices=[('puppy', 'puppy'), ('adult', 'adult'), ('senior', 'senior')], max_length=50)),
                ('labelrange', models.CharField(choices=[('new', 'new'), ('small dog', 'small dog'), ('variety pack', 'variety pack'), ('national trust', 'national trust'), ('other', 'other')], max_length=50)),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('pic1', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('pic2', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('pic3', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('pic4', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('pic5', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('nutrition_info', models.TextField()),
                ('feeding_guide', models.TextField()),
                ('deliver_info', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
