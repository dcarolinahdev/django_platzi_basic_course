"""Posts URLs."""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from posts import views

urlpatterns = [

    # path(
    #     route='',
    #     view=views.list_posts,
    #     name='list_posts'
    # ),

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='list_posts'
    ),

    path(
        route='posts/new/',
        view=views.create_post,
        name='create'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
