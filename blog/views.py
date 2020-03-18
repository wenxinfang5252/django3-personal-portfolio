from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #only show most recent
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id) #if nothing found, show 404 otherwise get this one object
    return render(request, 'blog/detail.html', {'blog':blog})
