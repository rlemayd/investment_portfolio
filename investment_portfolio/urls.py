from django.contrib import admin
from django.urls import path, include
from portfolio_manager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', getPortfolioRequest, name="main"),
    path('dashboard/', retrieveData, name="retrieve_data"),
    path('api/', include('portfolio_manager.urls')),
]

handler404 = failed_404_view