from datetime import timedelta
from django.utils import timezone
from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Portfolio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    assets = models.ManyToManyField(Asset, through='AssetPortfolio')
    initial_value = models.DecimalField(max_digits=20, decimal_places=2, default=1000000000)
    
    def daily_value(self, date):
        # get the value of the portfolio on the previous day
        date_before = date - timedelta(days=1)
        first_day_object = PortfolioDailyValue.objects.filter(portfolio=self, date=date_before).exists()
        
        # if there is no previous value, use the initial value
        if not first_day_object:
            first_day_value = self.initial_value
            portfolio_daily_value = PortfolioDailyValue(portfolio=self, date=date, value=first_day_value)
            portfolio_daily_value.save()
            return first_day_value

        asset_portfolios = self.assetportfolio_set.all()
        daily_value = sum(ap.quantity * AssetPrice.objects.get(asset=ap.asset, date=date).price for ap in asset_portfolios)

        portfolio_daily_value = PortfolioDailyValue(portfolio=self, date=date, value=daily_value)
        portfolio_daily_value.save()
        return daily_value
    
    def get_weights_by_date_range(self, start_date, end_date):
        weights_by_date = {}
        current_date = start_date
        while current_date <= end_date:
            try:
                total_value = PortfolioDailyValue.objects.get(portfolio=self, date=current_date).value #obtain portfolio value
                asset_portfolios = AssetPortfolio.objects.filter(portfolio=self) #all assets from portfolio
                for ap in asset_portfolios:
                    asset_value = ap.quantity * AssetPrice.objects.get(date=current_date, asset=ap.asset).price
                    weight = asset_value / total_value
                    if str(current_date) in weights_by_date:
                        weights_by_date[str(current_date)].append({'asset': ap.asset.name, 'weight': weight})
                    else:
                        weights_by_date[str(current_date)] = [{'asset': ap.asset.name, 'weight': weight}]
            except PortfolioDailyValue.DoesNotExist:
                pass
            current_date += timedelta(days=1)
        return weights_by_date
    
class PortfolioDailyValue(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    value = models.DecimalField(max_digits=20, decimal_places=2)

class AssetPortfolio(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=3)
    quantity = models.DecimalField(max_digits=12, decimal_places=5, null=True)

class AssetPrice(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
