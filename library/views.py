from django.shortcuts import render
from django.views.generic import ListView,DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from library.models import Library
from .forms import PostForm

# Create your views here.

def library(request):
    """ queries all blog from the database and sends a template based the device"""
    books = Library.objects.order_by('-datePosted')
    content = {
        "books" : books
    }
    return render(request, 'library/library.html', content)

class BookDetailView(DetailView):
    """ this class show the detail of a news"""
    model = Library
    template_name ="library/library-detail.html"
    context_object_name = 'book'


class BookAddView(CreateView):
    """used to create form and post a News with the same class"""
    model = Library
    form_class = PostForm
    template_name="library/library_form.html"

    
    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)
