from django.shortcuts import render, get_object_or_404

from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.utils import timezone

from django.urls import reverse_lazy

from django.db.models import Q


class PostListView(LoginRequiredMixin, ListView):
    from .models import Post

    model = Post
    template_name = 'blog/home.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(Q(title__icontains=query) |
                                             Q(content__icontains=query))
        return self.model.objects.all()


class PostDetailView(LoginRequiredMixin, DetailView):
    from .models import Post

    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    from .models import Post
    from .forms import PostForm

    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_posted = timezone.now()
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    from .models import Post
    from .forms import PostForm

    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # success_url = reverse_lazy('blog-detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_posted = timezone.now()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    from .models import Post

    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(LoginRequiredMixin, ListView):
    from .models import Post

    model = Post
    template_name = 'blog/user_post.html'
    paginate_by = 5

    def get_queryset(self):
        from .models import User
        # user= self.request.GET.get('username')
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return self.model.objects.filter(author=user)


def about(request):
    template_name = 'blog/about.html'
    return render(request, template_name=template_name)
