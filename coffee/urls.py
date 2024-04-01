"""
URL configuration for coffee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from accounts.Api.views import AccountListCreateView
from register.Api.views import RegisterListCreateView
from recipes.Api.views import RecipeListCreateView, IngredientListCreateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = SimpleRouter()

router.register("api/accounts", AccountListCreateView, basename="accounts-list")

router.register("api/register", RegisterListCreateView, basename="register-list")

router.register("api/recipes", RecipeListCreateView, basename="recipes-list")

router.register("api/ingredient", IngredientListCreateView, basename="ingredient-list")

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/token-auth/", views.obtain_auth_token),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Rota para obter o token de acesso
    path("api/token-refresh/", TokenRefreshView.as_view(), name='token_refresh'),  # Rota para refresh token
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]+router.urls
