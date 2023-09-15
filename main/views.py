from django.conf import settings
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.forms import ProductForm, VersionForm
from main.models import Product, Feedback, Version
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginRequiredMixin(LoginRequiredMixin):
    registration_url = reverse_lazy('users:register')

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            return super().handle_no_permission()
        return redirect(self.registration_url)

class ProductListView(CustomLoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(CustomLoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'main/Product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f"version_list_{self.object.pk}"
            version_list = cache.get(key)
            if version_list is None:
                version_list = self.object.version_set.all()
                cache.set(key, version_list)
        else:
            version_list = self.object.version_set.all()

        context['versions'] = version_list
        return context


class ProductCreateView(CustomLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')


class ProductUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(CustomLoginRequiredMixin, DeleteView):
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


class VersionListView(ListView):
    model = Version

class VersionDetailView(DetailView):
    model = Version

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm

class VersionDeleteView(DeleteView):
    model = Version

def create_version(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        version_form = VersionForm(request.POST)
        if version_form.is_valid():
            version = version_form.save(commit=False)
            version.product = product
            version.save()
    else:
        version_form = VersionForm()

    return render(request, 'Product_detail.html', {'product': product, 'version_form': version_form})



