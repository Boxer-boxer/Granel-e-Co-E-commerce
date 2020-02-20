"""granel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from catalog import views as catalog_views
from django.contrib.auth import views as auth_views
from users import views as users_views
from payments import views as payments_views

urlpatterns = [
    path('', catalog_views.home, name="home"),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/complete', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', users_views.register, name="register"),
    path('catalog/', catalog_views.catalog, name="catalog"),
    path('catalog/<int:pk>', catalog_views.detail, name="product-detail"),
    path('cart/', users_views.cart, name="cart"),
    path('update/', users_views.cart_update, name='cart_update'),
    path('order/', payments_views.OrderCreateView.as_view(), name='create-order'),
    path('order-detail/<slug:slug>', payments_views.OrderDetailView, name='order-detail'),

    path('test/', catalog_views.test, name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
