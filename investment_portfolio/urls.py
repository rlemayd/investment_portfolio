from django.contrib import admin
from django.urls import path, include
from portfolio_manager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio_manager.urls')),
]