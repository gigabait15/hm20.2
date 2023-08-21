from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from Blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'Blog/Blog_list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'object'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('blog:blog')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')

def activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_active:
        blog_item.is_active = False
    else:
        blog_item.is_active = True
    blog_item.save()
    return redirect(reverse('blog:blog'))

