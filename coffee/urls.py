
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from recipes.Api.views import RecipeListCreateView, IngredientListCreateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()


router.register("api/recipes", RecipeListCreateView, basename="recipes-list")

router.register("api/ingredient", IngredientListCreateView, basename="ingredient-list")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user/', include('user.api.urls')),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
<<<<<<< HEAD
]+router.urls
=======
]+router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> d88eb45d08068087e5310f2632a6f0c36a04b7be
