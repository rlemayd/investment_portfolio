import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from portfolio_manager.models import *
from portfolio_manager.utils.serializer import PortfolioDailyValueSerializer
from datetime import datetime, timedelta
from django.db.models import Min, Max
import requests
from django.urls import reverse
from django.shortcuts import redirect

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
    portfolio_name = request.GET.get('portfolio_name')

    if portfolio_name:
        portfolio_given = Portfolio.objects.get(name=portfolio_name)
        start_date = datetime.strptime(request.GET.get('fecha_inicio'), "%y-%m-%d").date()
        end_date = datetime.strptime(request.GET.get('fecha_fin'), "%y-%m-%d").date()
        Vt = PortfolioDailyValue.objects.filter(date__range=[start_date, end_date], portfolio=portfolio_given)
        
    else:
        start_date = datetime.strptime(request.GET.get('fecha_inicio'), "%d-%m-%y").date()
        end_date = datetime.strptime(request.GET.get('fecha_fin'), "%d-%m-%y").date()
        Vt = PortfolioDailyValue.objects.filter(date__range=[start_date, end_date])

    serializer = PortfolioDailyValueSerializer(Vt, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAssetsWeight(request):
    portfolio_name = request.GET.get('portfolio_name')

    if portfolio_name:
        start_date = datetime.strptime(request.GET.get('fecha_inicio'), "%y-%m-%d").date()
        end_date = datetime.strptime(request.GET.get('fecha_fin'), "%y-%m-%d").date()
        portfolio_given = Portfolio.objects.get(name=portfolio_name)
        """
        assets_weight = {
                    'portfolio_name': portfolio_given.name,
                    'assets': AssetPrice.objects.filter(asset__in=portfolio_given.assets.all(), date__range=[start_date, end_date]).values('asset__name','date','price'),
                }
        """
        assets_weight = {
                    'portfolio_name': portfolio_given.name,
                    'assets': portfolio_given.get_weights_by_date_range(start_date, end_date),
                }
    else:
        start_date = datetime.strptime(request.GET.get('fecha_inicio'), "%d-%m-%y").date()
        end_date = datetime.strptime(request.GET.get('fecha_fin'), "%d-%m-%y").date()
        assets_weight = []
        for portfolio in Portfolio.objects.all():
            """
            assets_weight.append({
                    'portfolio_name': portfolio.name,
                    'assets': AssetPrice.objects.filter(date__range=[start_date, end_date]).values('asset__name','date','price'),
                })
            """
            assets_weight.append({
                    'portfolio_name': portfolio.name,
                    'assets': portfolio.get_weights_by_date_range(start_date, end_date),
                })
    return Response(assets_weight)

def getPortfolioRequest(request):
    context = {"portfolios": Portfolio.objects.all()}
    return render (request,'retrieve_data.html', context)

def retrieveData(request):
    portfolio_name = request.GET.get('portfolio_name')
    date_range = request.GET.get('date_range')
    
    start_date_str, end_date_str = date_range.split(' - ')
    start_date = datetime.strptime(start_date_str, '%m/%d/%Y')
    end_date = datetime.strptime(end_date_str, '%m/%d/%Y')

    # Format start and end dates for API request
    start_date_str_api = start_date.strftime('%y-%m-%d')
    end_date_str_api = end_date.strftime('%y-%m-%d')
    query_params = f'?portfolio_name={portfolio_name}&fecha_inicio={start_date_str_api}&fecha_fin={end_date_str_api}'

    values = requests.get(request.build_absolute_uri(reverse('portfolio_values') + query_params)).json()

    context = {"portfolio_name": portfolio_name,
               "portfolio_values": json.dumps(values, default=str),
               "asset_weights": json.dumps(requests.get(request.build_absolute_uri(reverse('assets_weight') + query_params)).json())}
    return render (request,'dashboard.html', context)

@api_view(['GET'])
def get_portfolio_date_ranges(request):
    portfolio_name = request.GET.get('portfolio_name')
    portfolio = Portfolio.objects.get(name=portfolio_name)

    portfolio_daily_values = PortfolioDailyValue.objects.filter(portfolio=portfolio)
    start_date, end_date = portfolio_daily_values.aggregate(Min('date'), Max('date')).values()
    start_date = start_date.strftime('%m/%d/%Y')
    end_date = end_date.strftime('%m/%d/%Y')

    data = {'start_date': start_date, 'end_date': end_date}

    return JsonResponse(data)

def failed_404_view(request, exception):
    return redirect('main')