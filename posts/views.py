"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Utilities
from datetime import datetime
import json

posts = [
	{
		'title': 'Sebastian de Belalcazar',
		'user': {
			'name': 'Carolina Hernandez',
			'picture': 'https://qph.fs.quoracdn.net/main-qimg-b80fb8d13f575f717fefb14dd759ded4'
		},
		'timestamp': datetime.now().strftime("%b %d, %Y - %H:%M horas"),
		'photo': 'https://90minutos.co/wp-content/uploads/2020/09/estatua-de-sebastian-de-belalcazar-6819a614-7621-45fa-90ed-16c1afc8529c-e1600469695128.jpg',
	},
	{
		'title': 'Ermita',
		'user': {
			'name': 'Gabriel Ortiz',
			'picture': 'https://pbs.twimg.com/profile_images/3091183641/339fb831e1199dac9934661550c726ea.jpeg'
		},
		'timestamp': datetime.now().strftime("%b %d, %Y - %H:%M horas"),
		'photo': 'https://www.elpais.com.co/files/article_main_small/uploads/2019/06/03/5cf5ddcd98ee9.jpeg',
	},
	{
		'title': 'Tres Cruces',
		'user': {
			'name': 'David Pabon',
			'picture': 'https://i.pinimg.com/474x/30/09/33/300933d32c514d41a2aba0aac3839833.jpg'
		},
		'timestamp': datetime.now().strftime("%b %d, %Y - %H:%M horas"),
		'photo': 'https://hablemosdeculturas.com/wp-content/uploads/2018/12/cerro-de-las-tres-cruces-en-cali-1-e1544207937949.jpeg',
	}
]

@login_required
def list_posts(request):
	"""List existing posts."""
	return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
	"""Create new post view."""
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('list_posts')

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
