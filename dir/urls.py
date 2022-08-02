from django.urls import path

from .views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='home'),

    path('category/<int:category_id>/', get_category, name='category'),

    path('test/', test),
]

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)