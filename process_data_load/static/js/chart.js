var chart;

function requestData() {
    $.ajax({
        url: '/live_resource',
        success: function(point) {
            console.log(point)
            var series = chart.series[0],
                shift = series.data.length > 50;

            chart.series[0].addPoint(point, true, shift);

            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Realtime machine data'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'percent',
                margin: 80
            }
        },
        series: [{
            name: 'E01',
            data: []
        }]
    });
});