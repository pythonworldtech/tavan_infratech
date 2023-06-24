# Generated by Django 3.2.8 on 2023-05-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/download/uploads/gallery_images/')),
                ('heading', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
