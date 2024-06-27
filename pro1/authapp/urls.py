from django.urls import path
from .views import *
urlpatterns = [
    path("siv/",siview),
    path("liv/",liview),
    path("lov/",loview),
]