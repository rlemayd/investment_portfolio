from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('porfolio_dates/', views.get_portfolio_date_ranges, name="get_portfolio_date_ranges"),
    path('assets/', views.getAssets),
    path('assets/<str:name>/', views.getAsset),
    path('portfolio_values/', views.getPortfolioValues, name="portfolio_values"),
    path('asset_weights/', views.getAssetsWeight, name="assets_weight"),
]