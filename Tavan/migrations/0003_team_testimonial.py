# Generated by Django 3.2.8 on 2023-05-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tavan', '0002_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/download/uploads/gallery_images/')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/download/uploads/gallery_images/')),
                ('message', models.TextField(max_length=250)),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
