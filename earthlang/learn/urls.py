from django.urls import path
#now import the views.py file into this code
from . import views
app_name = 'learn'
urlpatterns=[

  path('', views.index, name="index"),
  path('spanish', views.spanish, name="spanish"),
  path('french', views.french, name="french"),
  path('german', views.german, name="german"),
  path('chinese', views.chinese, name="chinese"),
  ]