from django.urls import path

from core.views import *
from orders.views import OrderView, AddOrderView, OrderDetailsView, MarkAsDelivered,  NotDeliveredStatus,DeliveredStatus

urlpatterns = [
    path('OrderView/', OrderView.as_view(), name='OrderView'),
    path('AddOrderView/', AddOrderView.as_view(), name='AddOrderView'),
    path('OrderDetailsView/', OrderDetailsView.as_view(), name='OrderDetailsView'),
    path('MarkAsDelivered/<int:pk>/', MarkAsDelivered.as_view(), name='MarkAsDelivered'),
    path('DeliveredStatus/<int:pk>/', DeliveredStatus.as_view(), name='DeliveredStatus'),
    path('NotDeliveredStatus/<int:pk>/', NotDeliveredStatus.as_view(), name='NotDeliveredStatus'),


]