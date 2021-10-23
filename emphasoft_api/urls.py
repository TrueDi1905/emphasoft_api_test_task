from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', include('djoser.urls.authtoken')),
    path('api/v1/users/', include('users.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
