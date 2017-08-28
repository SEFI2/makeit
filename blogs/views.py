from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from . import models
from . import forms
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from urllib.parse import urlparse
import os.path



@login_required
def CreateBlog(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            blog = models.Blog()
            blog.author = request.user
            blog.content = form.cleaned_data.get('content')
            blog.title = form.cleaned_data.get('title')
            blog.save()
            return redirect('/blogs/')
    else:
        form = forms.BlogForm()
    return render(request, 'blogs/blog_form.html' , {'form':form})

@login_required
def EditBlog(request, pk):
    if pk:
        blog = get_object_or_404(models.Blog, pk=pk)
    else:
        blog = models.Blog(author=request.user)

    if blog.author.id != request.user.id:
        return redirect('/blogs/')

    if request.POST:
        form = forms.BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/blogs/')
    else:
        form = forms.BlogForm(instance=blog)
    return render(request, 'blogs/blog_form.html' , {'form':form})


class BlogLook(DetailView):
    template_name = 'blogs/oneblog.html'
    model = models.Blog
    def post(self, request, *args, **kwargs):
        comment = request.POST.get("comment" , "")
        blog = models.Blog.objects.get(pk=kwargs['pk'])
        models.BlogComment.objects.create(comment = comment,blog=blog,user=request.user)
        return redirect('/blogs/' + str(kwargs['pk']))


class AllBlogs(ListView):
    template_name = 'blogs/all_blogs.html'
    model = models.Blog
    queryset = models.Blog.objects.all()


@login_required
def Activities(request , article_type, activity_type, pk):
    if article_type == 'blog':
        blog = models.Blog.objects.get(pk=pk)
        done_activity = models.BlogActivity.objects.filter(blog=blog).filter(user=request.user).filter(activity_type=activity_type)
        if done_activity.exists():
            done_activity.delete()
        else:
            models.BlogActivity.objects.create(blog=blog, user=request.user,activity_type=activity_type)
        blog.author.profile.change_rating()

        print ("Here it is")

    else:
        blog_comment = models.BlogComment.objects.get(pk=pk)
        done_activity = models.BlogCommentActivity.objects.filter(blog_comment=blog_comment).filter(user=request.user).filter(activity_type=activity_type)
        if done_activity.exists():
            done_activity.delete()
        else:
            models.BlogCommentActivity.objects.create(blog_comment=blog_comment, user=request.user,activity_type=activity_type)

    return redirect(request.META.get('HTTP_REFERER', '/'))

