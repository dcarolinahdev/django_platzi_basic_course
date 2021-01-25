"""Users URLs."""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# View
from users import views


urlpatterns = [
    # Management
    path(
        route='login/',
        view=views.login_view,
        name='login'
        ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
        ),
    path(
        route='signup/',
        view=views.signup_view,
        name='signup'
        ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update_profile'
        )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
