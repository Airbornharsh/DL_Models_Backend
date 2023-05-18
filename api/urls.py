from django.urls import path
from .views import *

urlpatterns = [
    path("flower-detection-5", Flower_Detection_5.as_view()),
    path("face-expression-detection", Face_Expression_Detection.as_view()),
]
