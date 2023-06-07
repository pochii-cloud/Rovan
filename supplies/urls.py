from django.urls import path

from core.views import *
from supplies.views import AddSuppliesView, AddSuppliersView, SupplyDetails, SupplyStatus,SupplyStatuSupplied,SupplyStatuNotSupplied

urlpatterns = [
    path('AddSuppliesView/', AddSuppliesView.as_view(), name='AddSuppliesView'),
    path('AddSuppliersView/', AddSuppliersView.as_view(), name='AddSuppliersView'),
    path('SupplyDetails/', SupplyDetails.as_view(), name='SupplyDetails'),
    path('SupplyStatus/<int:pk>/', SupplyStatus.as_view(), name='SupplyStatus'),
    path('SupplyStatuSupplied/<int:pk>/', SupplyStatuSupplied.as_view(), name='SupplyStatuSupplied'),
    path('SupplyStatuSupplied/<int:pk>/', SupplyStatuSupplied.as_view(), name='SupplyStatuSupplied'),
    path('SupplyStatuNotSupplied/<int:pk>/', SupplyStatuNotSupplied.as_view(), name='SupplyStatuNotSupplied'),

]
