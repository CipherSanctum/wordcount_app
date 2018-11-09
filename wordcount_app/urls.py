from django.urls import path
from . import views


app_name = 'wordcount_app'


urlpatterns = [
    path('', views.wordcount, name='wordcount'),
    path('results/', views.wordcount_results, name='wordcount_results'),
]
