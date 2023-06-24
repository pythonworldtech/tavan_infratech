from django.contrib import admin
from django.urls import path
from Tavan.views import *
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='index'),
    path('about_us',about_us, name='about_us'),
    path('services',services, name='services'),
    path('project',project, name='project'),
    path('achievements',achievements,name='achievements'),
    path('contact',Contact.as_view(),name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
