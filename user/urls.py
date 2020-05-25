from django.urls import path
from django.contrib.auth import views as auth_views
from . views import register, profile, SearchView

app_name = "user"
urlpatterns = [
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('search/', SearchView, name="search"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/password_reset_done.html'), name='password-reset-done'),
    path('password-reset/comfirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password-reset-confirm'),
]
