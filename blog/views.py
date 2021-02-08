from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Function based views
def home(request):
    """
    displays the blog's data fields

    :param request: HttpRequest object which contains the data 
    :return: renders the template home.html
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    """
    displays about page details

    :param request: HttpRequest object which contains the data 
    :return: renders the template about.html
    """
    return render(request, 'blog/about.html', {'title': 'About'})



# Class based views
class PostListView(ListView):
    """
    creates a list view for the blog posts on the home page

    :params ListView: Class
    """
    model = Post
    template_name = 'blog/home.html' # convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # the - is used to return blog posts in reverse order on the home page

class PostDetailView(DetailView):
    """
    creates a detail view for the individual blog - created the convention template post_detail.html

    :params DetailView: Class
    """
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    creates a create view to create new blog posts

    :params LoginRequiredMixin: Class, adds a login functionality to the view
    :params CreateView: Class
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        ensures the author of the post is the user that's currently logged in

        :params form: form
        :return: returns the form_valid method on the parent class
        """
        form.instance.author =  self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    creates a update view to when a blog is updated

    :params LoginRequiredMixin: Class, adds a login functionality to the view
    :params UserPassesTestMixin: Class, ensures user is the author of the post
    :params UpdateView: Class
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        ensures the author of the post is the user that's currently logged in

        :params form: form
        :return: returns the form_valid method on the parent class
        """
        form.instance.author =  self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        ensures current user is the author of the blog post

        :return: allow (or disallow) the user to edit the post
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    creates a delete view to when a blog is deleted

    :params LoginRequiredMixin: Class, adds a login functionality to the view
    :params UserPassesTestMixin: Class, ensures user is the author of the post
    :params UpdateView: Class
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """
        ensures current user is the author of the blog post

        :return: allow (or disallow) the user to delete the post
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False