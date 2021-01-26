"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class PostsFeedView(LoginRequiredMixin, ListView):
	"""Return all published posts."""

	model = Post
	ordering = ('-created',)
	template_name = 'posts/feed.html'
	paginate_by = 2
	context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
	"""Return post detail."""

	template_name = 'posts/detail.html'
	queryset = Post.objects.all()
	context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
	"""Create a new post."""

	template_name = 'posts/new.html'
	form_class = PostForm
	success_url = reverse_lazy('posts:list_posts')

	def get_context_data(self, **kwargs):
		"""Add user and profile to context."""
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context
