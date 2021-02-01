
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('orders/', include('orders.urls')),
    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),  # <-- And here


]
