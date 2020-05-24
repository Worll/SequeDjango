"""seque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path, re_path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('social/', include('social_django.urls')),
    path('admin/', admin.site.urls),
    path("", include("backend.urls")),
    re_path(r'^api/token(\/)?$', jwt_views.TokenObtainPairView.as_view(),
            name='token_obtain_pair'),
    re_path(r'^api/token/refresh(\/)?$',
            jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
