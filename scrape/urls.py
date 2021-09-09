from django.urls import path
from scrape import views

app_name = 'scrape'

urlpatterns = [
    path('', views.home,name='home'),
    path('compare/',views.compare,name='compare'),
    path('send/',views.send,name='send'),
]
