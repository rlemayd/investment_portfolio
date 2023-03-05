from datetime import datetime
import pandas as pd

from portfolio_manager.models import Asset, Portfolio, AssetPortfolio, AssetPrice


def populate_data():
    df_weights = pd.read_excel("../datos.xlsx", sheet_name="weights")
    df_prices = pd.read_excel("../datos.xlsx", sheet_name="Precios")

    portfolio_names = list(df_weights.columns[2:])
    assets_names = df_weights[f'{df_weights.columns[1]}']
    initial_portfolio_value = 1000000000
    
    for portfolio_name in portfolio_names:
        # Create a Portfolio object
        portfolio = Portfolio(name=portfolio_name)

        # Save portfolio object to the database
        portfolio.save()
    
    for index, row in df_weights.iterrows():
        # Create an Asset object
        asset = Asset(name=row['activos'])

        # Save the objects to the database
        asset.save()

        # Create AssetPortfolio to associate asset with portfolio
        for portfolio_name in portfolio_names:
            if float(row[f"{portfolio_name}"]) != 0:
                asset_portfolio = AssetPortfolio(asset=asset,
                                                 portfolio=Portfolio.objects.get(name=portfolio_name),
                                                 weight=row[f'{portfolio_name}'])
                asset_portfolio.quantity = (asset_portfolio.weight * initial_portfolio_value)/df_prices[row['activos']][0]
                asset_portfolio.save()
                
        
        
    for index, row in df_prices.iterrows():
        for asset_name in assets_names:
            asset=Asset.objects.get(name=asset_name)
            asset_price = AssetPrice(asset=asset,
                                     date=row['Dates'],
                                     price=row[f'{asset_name}'])
            asset_price.save()
        
        for portfolio_name in portfolio_names:
            portfolio = Portfolio.objects.get(name=portfolio_name)
            portfolio.daily_value(row['Dates'])