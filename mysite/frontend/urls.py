from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.glitchsubmit, name='glitchsubmit'),
    path('hw/day<int:day>/', views.view, name='viewhw'),
    
]