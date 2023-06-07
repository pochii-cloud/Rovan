from django.urls import path

from core.views import *

urlpatterns = [
    path('', BaseView.as_view(), name='BaseView'),
    path('UtilityCategoryView/', UtilityCategoryView.as_view(), name='UtilityCategoryView'),
    path('AddCategoryView/', AddCategoryView.as_view(), name='AddCategoryView'),
    path('DeleteCategoryView/<int:pk>/', DeleteCategoryView.as_view(), name='DeleteCategoryView'),
    path('ProductUtilityView/', ProductUtilityView.as_view(), name='ProductUtilityView'),
    path('AddProductView/', AddProductView.as_view(), name='AddProductView'),
    path('ErrorPageView/', ErrorPageView.as_view(), name='ErrorPageView'),
    path('ChartsView/', ChartsView.as_view(), name='ChartsView'),
    path('TablesView/', TablesView.as_view(), name='TablesView'),
    path('error_404/', error_404, name='error_404'),

]
