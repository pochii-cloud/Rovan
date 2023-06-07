from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from supplies.models import Suppliers, Supplies


class AddSuppliesView(View):
    def get(self, request):
        return render(request, 'add_supplies.html')

    def post(self, request):
        products = request.POST.get('products')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        supplies = Supplies()
        supplies.user = request.user
        supplies.supplies = products
        supplies.quantity = quantity
        supplies.cost = cost
        supplies.supply_date = date
        supplies.save()
        return HttpResponse('submitted')


class AddSuppliersView(View):
    def get(self, request):
        return render(request, 'add_suppliers.html')

    def post(self, request):
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        suppliers = Suppliers()
        suppliers.username = username
        suppliers.phone = phone
        suppliers.address = address
        suppliers.location = location
        suppliers.save()
        return HttpResponse('submitted')


class SupplyDetails(TemplateView):
    template_name = 'check_supplies.html'

    def get_context_data(self, **kwargs):
        context = super(SupplyDetails, self).get_context_data(**kwargs)
        context['supplies'] = Supplies.objects.all()
        return context


class SupplyStatus(View):
    def get(self, request, pk):
        supplies = Supplies.objects.get(pk=pk)
        context = {'supplies': supplies}
        return render(request, 'supplied.html', context)

    def post(self, request, pk):
        supplies = Supplies.objects.get(pk=pk)
        context = {'supplies': supplies}
        return render(request, 'supplied.html', context)


class SupplyStatuSupplied(View):
    def get(self, request, pk):
        supplies = Supplies.objects.get(pk=pk)
        if not supplies.supplied:
            supplies.supplied = True
            supplies.save()
            messages.info(request, 'Supply details updated successfully')
            return redirect('SupplyDetails')
        elif supplies.supplied:
            messages.info(request, 'Supply details updated successfully')
            return redirect('SupplyDetails')
        context = {'supplies': supplies}
        return render(request, 'supplied.html', context)

    def post(self, request, pk):
        return render(request, 'supplied.html')


class SupplyStatuNotSupplied(View):
    def get(self, request, pk):
        supplies = Supplies.objects.get(pk=pk)
        if supplies.supplied:
            supplies.supplied = False
            supplies.save()
            messages.info(request, 'Supply details updated successfully')
            return redirect('SupplyDetails')
        elif not supplies.supplied:
            messages.info(request, 'Supply details updated successfully')
            return redirect('SupplyDetails')
        context = {'supplies': supplies}
        return render(request, 'supplied.html', context)

    def post(self, request, pk):
        return render(request, 'supplied.html')
