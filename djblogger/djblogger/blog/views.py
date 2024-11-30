from typing import Any
from django.db.models.query import QuerySet
from .models import Post
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from .forms import PostSearchForm


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):

        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, "./blog/single.html", {"post": post, "related": related})


class TagListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements-tags.html"
        return "blog/tags.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug__in=[self.kwargs["tag"]])

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context


class PostSearchView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = "posts"
    form_class = PostSearchForm

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements-search.html"
        return "blog/search.html"

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Post.objects.filter(title__icontains=form.cleaned_data["q"])
        return []
