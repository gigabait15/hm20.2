from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import contact, ProductCreateView, ProductDetailView, ProductUpdateView, ProductListView, \
    ProductDeleteView, activity


app_name = 'main'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('view/<int:pk>/', never_cache(cache_page(60)(ProductDetailView.as_view())), name='view_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('activity/<int:pk>/', activity, name='activity'),
]