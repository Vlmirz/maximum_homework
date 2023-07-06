from django.urls import path
from .views import homework


urlpatterns = [
    path('lesson_4', homework),
]