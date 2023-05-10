from homepagesite import views
from django.urls import path

app_name = 'homepagesite'

urlpatterns = [
    path('', views.index, name='index'),
]
