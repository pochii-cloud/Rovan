from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, DeleteView

from core.forms import ProductForm
from core.models import Category, Product, Sales
from orders.models import Orders
from supplies.models import Supplies


class BaseView(LoginRequiredMixin, View):
    login_url = '/accounts/LoginPageView/'

    def get(self, request):
        qs = Product.objects.all()[0:5]
        q = Sales.objects.all()[0:5]
        category_count = Category.objects.filter(user=request.user).count()
        product_count = Product.objects.filter(user=request.user).count()
        total_sales = Sales.objects.filter(user=request.user).count()
        pending_orders = Orders.objects.filter(delivered=False).count()
        pending_supplies = Supplies.objects.filter(supplied=False).count()
        context = {'qs': qs, 'q': q, 'category_count': category_count,
                   'total_sales': total_sales,
                   'product_count': product_count,
                   'pending_orders': pending_orders,
                   'pending_supplies': pending_supplies
                   }
        return render(request, 'index.html', context)

    def post(self, request):
        return render(request, 'index.html')


class UtilityCategoryView(View):
    template_name = 'categories.html'

    def get(self, request):
        category = Category.objects.filter(user=request.user)
        context = {'category': category}
        return render(request, 'categories.html', context)


class AddCategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'categories.html', {'category': category})

    def post(self, request):
        category = request.POST.get('category')
        categories = Category()
        categories.name = category
        categories.user = request.user
        categories.save()
        messages.info(request, 'category added successfully')
        return render(request, 'categories.html')


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'Confirm_delete.html'
    success_url = '/'


class ProductUtilityView(View):
    def get(self, request):
        category = Category.objects.all()
        form = ProductForm()
        context = {'category': category, 'form': form}
        return render(request, 'Products.html', context)

    def post(self, request):
        category = Category.objects.all()
        form = ProductForm()
        context = {'category': category, 'form': form}
        return render(request, 'Products.html', context)


class AddProductView(FormView):
    form_class = ProductForm
    success_url = '/'
    template_name = 'Products.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ErrorPageView(TemplateView):
    template_name = '404.html'


class ChartsView(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Product.objects.all()[0:5]
        context['q'] = Sales.objects.all()[0:5]
        return context


class TablesView(TemplateView):
    template_name = 'tables.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)
