from django.contrib import admin
from django.apps import apps

from .models import Asset, AssetPortfolio, AssetPrice, Portfolio, PortfolioDailyValue

admin.site.register(Asset)
admin.site.register(Portfolio)
admin.site.register(PortfolioDailyValue)
admin.site.register(AssetPortfolio)
admin.site.register(AssetPrice)
