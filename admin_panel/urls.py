from django.urls import path

from admin_panel import views as admin_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin',admin_views.admin,name='admin'),
    path('add_office',admin_views.add_office,name='add_office'),
    path('add_country',admin_views.add_country,name='add_country'),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)