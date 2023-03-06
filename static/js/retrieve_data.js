$('#portfolio-select').on('change', function () {
    $.ajax({
      url: getPortfolioDateRangesUrl(),
      data: { portfolio_name: $(this).val() },
      dataType: 'json',
      success: function (data) {
        $('#date-range-picker').show();
        $('input[name="daterange"]').daterangepicker({
          minDate: data.start_date,
          maxDate: data.end_date,
          startDate: data.start_date,
          endDate: data.end_date,
        });
      },
    });
  });

$('#submit-button').on('click', function () {
var portfolio_name = $('#portfolio-select').val();
var date_range = $('input[name="daterange"]').val();

window.location.href =
    getRetrieveDataUrl() +
    '?portfolio_name=' +
    portfolio_name +
    '&date_range=' +
    date_range;
});