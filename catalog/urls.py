from django.urls import path

from catalog.views import con, hom

urlpatterns = [
    path('', hom),
    path('contacts/', con),
]