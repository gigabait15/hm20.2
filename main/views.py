from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Product, Feedback


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'image', 'category', 'price', 'date_burn', 'date')
    success_url = reverse_lazy('main:home')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'image', 'category', 'price', 'date_burn', 'date')
    success_url = reverse_lazy('main:home')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:home')

def activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True
    product_item.save()
    return redirect(reverse('main:home'))

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()
    return render(request, 'main/contact.html')

