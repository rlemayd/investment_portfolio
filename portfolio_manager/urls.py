from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('assets/', views.getAssets),
    path('assets/<str:name>/', views.getAsset),
    path('portfolio_values/', views.getPortfolioValues),
    path('asset_weights/', views.getAssetsWeight),
]