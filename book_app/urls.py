"""book_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


# For sentry debug
def trigger_error(request):
    division_by_zero = 1 / 0


# Error handlers
handler404 = 'bookmarket.views.handler404'
# handler500 = 'bookmarket.views.handler500' # Not needed since Sentry captures these errors by default
handler403 = 'bookmarket.views.handler403'
handler400 = 'bookmarket.views.handler400'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('profile/', user_views.profile, name='profile'),
    path('profileUser/<username>/', user_views.profileUser, name='profileUser'),
    path('profileUserName/<username>/<inos>',
         user_views.profileUserName, name='profileUserName'),

    path('', include('bookmarket.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('users.urls')),
    path('messages/', include('postman.urls', namespace='postman')),
    path('sentry-debug/', trigger_error),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
