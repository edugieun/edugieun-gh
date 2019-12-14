from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('problems/', views.problem_list),
]
