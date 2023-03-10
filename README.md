# Investment Portfolio App

### Instructions for running the project

For this app, you need an .xlsx file, which needs to have two sheets:
1. The name needs to be "weights" and with this format:

| Fecha      | activos       | _portfolio1_name_ | _portfolio2_name_ |
|------------|---------------|-------------------|-------------------|
| _15-02-22_ | _asset1_name_ | _weight_value__   | _weight_value_    |
| _15-02-22_ | _asset2_name_ | _weight_value_    | _weight_value_    |
| _15-02-22_ | _asset3_name_ | _weight_value_    | _weight_value_    |

2. The name needs to be "Precios" and with this format:

| Fecha      | _asset1_name_  | _asset2_name_  | _asset3_name_  |   |
|------------|----------------|----------------|----------------|---|
| _15-02-22_ | _asset1_price_ | _asset2_price_ | _asset3_price_ |   |
| _16-02-22_ | _asset1_price_ | _asset2_price_ | _asset3_price_ |   |
| _17-02-22_ | _asset1_price_ | _asset2_price_ | _asset3_price_ |   |

After having this Excel file, you need to leave it at the same directory as the project with the name of datos.xlsx.

For installing all the required libraries, you can enter to a shell and go to the project directory and run this command, which will install every package needed for this project:
```shell
pip install -r requirements.txt
```

For populating the database of the project with the Excel file data, you need to run this command:
```shell
python manage.py populate
```
If you want to erase all the data stored, you need to put this command:
```shell
python manage.py flush
```

After populating the data, you can run the program with the following command:
```shell
python manage.py runserver
```

Once the project is running, you can enter the URL provided in the shell, and watch the behavior of a specific portfolio for a given date-range.

### Instructions for using the API

The API for this project is pretty simple, you can retrieve the Assets, check the portfolio values through a date range and the asset weights on a specific portfolio through a date range, the following commands will help you achieve this:

For getting all the Assets
```api
http://127.0.0.1:8000/api/assets
```

For getting a specific Asset
```api
http://127.0.0.1:8000/api/assets/<name_of_the_asset>
```

For getting the asset weights of all the portfolios during a date range
```api
http://127.0.0.1:8000/api/asset_weights/?fecha_inicio=<start_date>&fecha_fin=<end_date>
```

For getting all the portfolio values during a date range
```api
http://127.0.0.1:8000/api/portfolio_values/?fecha_inicio=<start_date>&fecha_fin=<end_date>
```
