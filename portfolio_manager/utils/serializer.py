from rest_framework import serializers
from portfolio_manager.models import Asset, AssetPortfolio, Portfolio, AssetPrice, PortfolioDailyValue

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asset
        fields="__all__"

class PortfolioDailyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=PortfolioDailyValue
        fields=('portfolio', 'date', 'value')