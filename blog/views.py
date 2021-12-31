from django.db.models import fields
from django.db.models.base import Model
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import re
from django.urls import reverse
from django.views.generic import ListView,DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import  CommentForm, PostForm
from django.contrib.auth.models import User
from . models import Blog, Comment
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 




# Create your views here. 
def mobile(request):
    """ request from the device and checks if it is a mobile or not"""
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False


def home(request):
    return render(request, 'home.html')


def blog(request):
    """ queries all blog from the database and sends a template based the device"""
    blogs = Blog.objects.order_by('-blog_datePosted')
    content = {
        "blogs" : blogs
    }
    return render(request, 'blog/blog.html', content)




class BlogDetailView(DetailView):
    """ this class show the detail of a blog"""
    model = Blog
    template_name ="blog/blog-detail.html"
    
    
    def  get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        
        # connects to the blog model and creates a blog object with the primary key 
        likes_connected = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # get the total likes from the blog object
        total_likes = likes_connected.likes.count()
        context['total_likes'] = total_likes
        liked = False
        # checks if the user has liked the blog 
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        
        pk = self.kwargs["pk"]

        form = CommentForm()
        post = get_object_or_404(Blog, pk=pk)
        comments = post.comments.all()
        
        category = likes_connected.blog_category
        print(category)
        others = Blog.objects.filter(blog_category=category).order_by("blog_datePosted").exclude(pk=pk)
        
        context['total_comments'] = post.comments.count()
        context['post'] = post
        context['comments'] = comments
        context['form'] = form 
        context['others'] = others 
        
        return context
    


    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        form = CommentForm(self.request.POST)
        self.object = self.get_object()
        comment = None

        post = get_object_or_404(Blog, pk=pk)
        name = get_object_or_404(User, id=self.request.user.id)
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            body = form.cleaned_data['body']

            comment = form.save(commit=False)
            comment.blog = post
            comment.name = name
            print(f"{comment.blog} | {comment.name}")
            comment.save()
             
            
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)
            
  

class BlogAddView(CreateView):
    """used to create form and post a blog with the same class"""
    model = Blog
    form_class = PostForm
    #template_name="blog/blog_form.html"

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
      
class BlogUpdateView(UpdateView):
    """used to create form and edit a blog with the same class"""
    model = Blog
    form_class = PostForm
    template_name="blog/update_form.html"
    # fields = "__all__"
    
     
class BlogDeleteView(DeleteView):
    """used to delete a blog with the same class"""
    model = Blog
    template_name = "blog/blog-delete.html"
    fields = "__all__"
    success_url = reverse_lazy('blogs')




def LikeView(request, pk):
    post = get_object_or_404(Blog, pk=request.POST.get("blog_Id"))      
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blogdetail', args=[str(pk),]))



class CommentView(CreateView):
    """used to create form and comment a blog with the same class"""
    model = Comment
    form_class = CommentForm
    # fields = ['body',]
    template_name = "blog/comment_section.html"

     
    def form_valid(self, form):
        # print("this is the username " + self.request.user.username)
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        ok = form.instance.blog
        form.instance.name = self.request.user.username
        # print('this is the username     :   ' + form.instance.name )
        return super().form_valid(form)



class Category(ListView):
    template_name="blog/blog.html"
    context_object_name = 'blogs'
    def get_queryset(self, *args, **kwargs):     
        category = self.kwargs["blog_category"]
        return Blog.objects.filter(blog_category=category)