"""Users URLs."""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# View
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
        ),
    path(
        route='logout/',
        view=auth_views.LogoutView.as_view(),
        name='logout'
        ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
        ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
        ),

    # Class Based Views
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
        )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
