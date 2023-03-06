//TODO: Create readme explaining everything
function changeDisplayGraphs() {
    var weightsChart = $('#weightsChartContainer')[0];
    var portfolioChart = $('#canvas')[0];
    if (weightsChart.style.display === 'none') {
      weightsChart.style.display = 'block';
      portfolioChart.style.display = 'none';
    } else {
      weightsChart.style.display = 'none';
      portfolioChart.style.display = 'block';
    }
  }
  $('#checkboxinp').click(changeDisplayGraphs);

  /* Function to create graph of portfolio values */
  var portfolioValues = getportfolioValues();
  var value_dates = portfolioValues.map(function (e) {
    return e.date;
  });
  var current_portfolio = portfolioValues[0].portfolio;
  var values = portfolioValues.map(function (e) {
    return e.value;
  });

  canvas.style.display = 'none';
  var ctx = canvas.getContext('2d');
  var config = {
    type: 'line',
    data: {
      labels: value_dates,
      datasets: [
        {
          label: `Portfolio ${current_portfolio}`,
          data: values,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  };
  var newChart = new Chart(ctx, config);
  /* End Function */

  //TODO: If the graph receives less than 7 days, it repeats the x-axis labels
  /* Function to create graph of asset weights */
  const assetWeights = getAssetWeights();
  const dates = Object.keys(assetWeights);
  const assets = assetWeights[dates[0]].map((a) => a.asset);
  var test = assets.map((asset) => (
    dates.map((date) => ({
      x: new Date(date),
      y: assetWeights[date].find((element) => element.asset === asset).weight,
    }))
  ))
  const dataPoints = assets.map((asset) => ({
    type: 'stackedArea',
    name: asset,
    showInLegend: true,
    dataPoints: dates.map((date) => ({
      x: new Date(date),
      y: assetWeights[date].find((element) => element.asset === asset).weight,
    })),
  }));
  const weightsChart = new CanvasJS.Chart('weightsChartContainer', {
    animationEnabled: true,
    title: {
      text: 'Asset Weights Over Time',
    },
    axisX: {
      valueFormatString: 'MMM DD, YYYY',
    },
    axisY: {
      title: 'Weight',
    },
    legend: {
      cursor: 'pointer',
      verticalAlign: 'top',
      horizontalAlign: 'center',
      dockInsidePlotArea: true,
    },
    toolTip: {
      shared: true,
    },
    data: dataPoints,
  });

  weightsChart.render();
  /* End of function to create graph of asset weights */