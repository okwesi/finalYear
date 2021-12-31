from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from news.models import News
from . forms import PostForm

# Create your views here.


def news(request): 
    news = News.objects.all().order_by('datePosted')
    context={
        'news': news
    }
    return render(request, 'news/news.html', context )


class NewsDetailView(DetailView):
    """ this class show the detail of a news"""
    model = News
    template_name ="news/news-detail.html"
    
    
    def  get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        
        # connects to the blog model and creates a blog object with the primary key 
        news_connected = get_object_or_404(News, pk=self.kwargs['pk'])
        
        category = news_connected.category
        others = News.objects.filter(category=category).order_by("datePosted").exclude(pk=self.kwargs['pk'])
        context['others'] = others 
        
        return context
    
    
class NewsAddView(CreateView):
    """used to create form and post a News with the same class"""
    model = News
    form_class = PostForm
    template_name="news/news_form.html"

    
    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    """used to create form and edit a News with the same class"""
    model = News
    form_class = PostForm
    template_name="news/update_form.html"



class NewsDeleteView(DeleteView):
    """used to delete a news with the same class"""
    model = News
    template_name = "news/news-delete.html"
    fields = "__all__"
    success_url = reverse_lazy('news')





    
class Category(ListView):
    template_name="news/news.html"
    context_object_name = 'news'
    def get_queryset(self, *args, **kwargs):     
        category = self.kwargs["category"]
        print(category)
        return News.objects.filter(category=category)