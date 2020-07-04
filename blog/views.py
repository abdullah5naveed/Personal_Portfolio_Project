from django.shortcuts import render, get_object_or_404
from .models import Blogs

def all_blog(request):
    blogs = Blogs.objects.order_by('-blog_date')

    return render(request, 'blog/all_blog.html', {'blogs':blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':blog})