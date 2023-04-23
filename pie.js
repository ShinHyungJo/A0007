google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart(pizza1, pizza2, pizza3, pizza4, pizza5) {
  var pizza = google.visualization.arrayToDataTable([
    ['Data', 'Value'],
    [pizza1, 0],
    [pizza2, 0],
    [pizza3, 0],
    [pizza4, 0],
    [pizza5, 0]
  ]);

  var options = {
    title: 'My Data',
    is3D: true
  };

  var chart = new google.visualization.PieChart(document.getElementById('pie_chart_div'));

  chart.draw(data, options);
}

$('#input_form').on('submit', function(e) {
  e.preventDefault();
  var pizza1 = $('#pizza1').val();
  var pizza2 = $('#pizza2').val();
  var pizza3 = $('#pizza3').val();
  var pizza4 = $('#pizza4').val();
  var pizza5 = $('#pizza5').val();
  drawChart(pizza1, pizza2, pizza3, pizza4, pizza5);
})