from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog-home'),
    url(r'^accounts/profile', views.update_profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/', views.upload_image, name='upload_image'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)