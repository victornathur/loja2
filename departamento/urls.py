from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('camisa/', views.camisa_list),
    path('camisa/<int:camisa_id>/', views.camisa_show),
    path('casual/', views.casual_list),
    path('casual/<int:casual_id>/', views.casual_show),

]
