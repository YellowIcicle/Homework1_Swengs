from django.urls import path

from HW1.HW1 import views

urlpatterns = [
    path('countries/', views.country_list),
    path('countries/<int:pk>/', views.country_detail),
    path('producers/', views.producer_list),
    path('producers/<int:pk>/', views.producer_detail),
    path('smartphones/', views.smartphone_list),
    path('smartphones/<int:pk>/', views.smartphone_detail)
]