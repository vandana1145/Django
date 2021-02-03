from django.urls import include, path

from .views import createStudent

urlpatterns = [
    path('', createStudent),
    path('create/', createStudent),
]