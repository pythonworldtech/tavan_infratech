from django.db import models

#====================================== Service Model ============================================
class Service(models.Model):
    image = models.ImageField(upload_to='image/download/uploads/gallery_images/',null=True,blank=True)
    heading = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.heading
#==================================================================================================
#==================================================================================================




#====================================== Contact Model ============================================
class Contact_us(models.Model):
    contact_id = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=250)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
#==================================================================================================
#==================================================================================================




#====================================== Testimonials Model ========================================
class Testimonial(models.Model):
    image = models.ImageField(upload_to='image/download/uploads/gallery_images/',null=True,blank=True)
    message = models.TextField(max_length=250)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
#==================================================================================================
#==================================================================================================



#====================================== Teams Model ================================================
class Team(models.Model):
    image = models.ImageField(upload_to='image/download/uploads/gallery_images/',null=True,blank=True)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
#==================================================================================================
#==================================================================================================
