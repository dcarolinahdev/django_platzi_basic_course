"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


# @login_required
# def list_posts(request):
# 	"""List existing posts."""
# 	posts = Post.objects.all().order_by('-created')

# 	return render(request, 'posts/feed.html', {'posts': posts})

class PostsFeedView(LoginRequiredMixin, ListView):
	"""Return all published posts."""

	model = Post
	ordering = ('-created',)
	template_name = 'posts/feed.html'
	paginate_by = 2
	context_object_name = 'posts'

@login_required
def create_post(request):
	"""Create new post view."""
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('posts:list_posts')

	else:
		form = PostForm()

	return render(
		request=request,
		template_name='posts/new.html',
		context={
			'form': form,
			'user': request.user,
			'profile': request.user.profile
		}
	)
