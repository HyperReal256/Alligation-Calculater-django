from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.alligation_form, name="form"),
    path('results/', views.results, name="results")
]