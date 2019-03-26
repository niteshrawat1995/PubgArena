from django.urls import path

from .views import *

urlpatterns = [
    path('maps/', MapListView.as_view(), name='list-map'),
    path('city/', CityListView.as_view(), name='list-city'),
    path('maps/<int:pk>/city/', CityListView.as_view(), name='list-map-city'),
    path('weapons/', WeaponListView.as_view(), name='list-weapon'),
    path('weapons/<int:pk>/', WeaponDetailView.as_view(), name='detail-weapon'),
    path('weapons/<int:pk>/', WeaponDetailView.as_view(), name='detail-weapon'),
    path('weapons/<int:pk>/maps/', MapWeaponListView.as_view(), name='detail-weapon-map'),
    path('weapons/demo/', WeaponView.as_view(), name='demo-ajax-view'),

]
