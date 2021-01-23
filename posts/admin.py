"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""Post admin."""

	list_display = ('user', 'profile', 'title', 'photo')

	search_fields = (
		'user__email',
		'user__username',
		'user__first_name',
		'user__last_name',
		'title'
	)

	list_filter = (
		'user__email',
		'user__username',
	)

	fieldsets = (
		('Owner', {
			'fields': (('profile', 'user'),),
		}),
		('Post', {
			'fields': (
				('title'),
				('photo')
			),
		}),
		('Metadata', {
			'fields': (('created', 'modified'),),
		}),
	)

	readonly_fields = ('created', 'modified')
