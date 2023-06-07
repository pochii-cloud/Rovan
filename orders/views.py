from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from orders.models import Orders


class OrderView(TemplateView):
    template_name = 'manageorders&supplies.html'


class AddOrderView(View):
    def get(self, request):
        return render(request, 'addorder.html')

    def post(self, request):
        ordered_by = request.POST.get('ordered_by')
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        orders = Orders()
        orders.ordered_by = ordered_by
        orders.phone = phone
        orders.product = product
        orders.quantity = quantity
        orders.cost = cost
        orders.date_ordered = date
        orders.save()
        return HttpResponse('submitted')


class OrderDetailsView(TemplateView):
    template_name = 'ordersdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Orders.objects.all()
        return context


class MarkAsDelivered(View):
    def get(self, request, pk):
        orders = Orders.objects.get(pk=pk)
        return render(request, 'delivered.html', {'orders': orders})

    def post(self, request, pk):
        return render(request, 'delivered.html')


class DeliveredStatus(View):
    def get(self, request, pk):
        orders = Orders.objects.get(pk=pk)
        if not orders.delivered:
            orders.delivered = True
            orders.save()
            messages.info(request, 'order details updated successfully')
            return redirect('OrderDetailsView')
        elif orders.delivered:
            messages.info(request, 'order details updated successfully')
            return redirect('OrderDetailsView')
        return render(request, 'delivered.html', {'orders': orders})

    def post(self, request, pk):
        return render(request, 'delivered.html')


class NotDeliveredStatus(View):
    def get(self, request, pk):
        orders = Orders.objects.get(pk=pk)
        if orders.delivered:
            orders.delivered = False
            orders.save()
            messages.info(request, 'order details updated successfully')
            return redirect('OrderDetailsView')
        elif not orders.delivered:
            messages.info(request, 'order details updated successfully')
            return redirect('OrderDetailsView')
        return render(request, 'delivered.html', {'orders': orders})

    def post(self, request, pk):
        return render(request, 'delivered.html')
