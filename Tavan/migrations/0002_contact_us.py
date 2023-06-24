# Generated by Django 3.2.8 on 2023-05-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tavan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=250)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
