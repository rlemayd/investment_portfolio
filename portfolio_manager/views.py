from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from portfolio_manager.models import PortfolioDailyValue, AssetPortfolio, Portfolio
from portfolio_manager.utils.serializer import PortfolioDailyValueSerializer
from datetime import datetime, timedelta

from portfolio_manager.models import Asset
from portfolio_manager.utils.serializer import AssetSerializer

@api_view(['GET'])
def getAssets(request):
    asset = Asset.objects.all()
    serializer = AssetSerializer(asset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAsset(request, name):
    asset = Asset.objects.get(name=name)
    serializer = AssetSerializer(asset, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPortfolioValues(request):
    start_date = datetime.strptime(request.GET.get('fecha_inicio'), "%d-%m-%y").date()
    end_date = datetime.strptime(request.GET.get('fecha_fin'), "%d-%m-%y").date()

    Vt = PortfolioDailyValue.objects.filter(date__range=[start_date, end_date])
    serializer = PortfolioDailyValueSerializer(Vt, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getAssetsWeight(request):
    start_date = datetime.strptime(request.GET.get('fecha_inicio'), "%d-%m-%y").date()
    end_date = datetime.strptime(request.GET.get('fecha_fin'), "%d-%m-%y").date()

    assets_weight = []
    for portfolio in Portfolio.objects.all():
        assets_weight.append({
                'portfolio_name': portfolio.name,
                'assets': portfolio.get_weights_by_date_range(start_date, end_date),
            })

    return Response(assets_weight)