from django.urls import path
from . import views

#Create url patterns

#Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
