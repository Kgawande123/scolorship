from django.urls import path
from .views import *
urlpatterns = [
    path("sv/",sview),
    path("hv/",hview),
    path("shv/",shview),
    path("uv/<int:pk>/",uview),
    path("dv/<int:k>/",dview),

]