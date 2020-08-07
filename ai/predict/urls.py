from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('predict/', views.PredictView.as_view()),
]