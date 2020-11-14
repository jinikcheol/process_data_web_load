const toggleBtn = document.querySelector('.navbar__toggleBtn');
const menu = document.querySelector('.navbar__menu');
const icons = document.querySelector('.navbar__icons');

toggleBtn.addEventListener('click', () => {
menu.classList.toggle('active');
icons.classList.toggle('active');
});

var chart = null; // Define global variables
var data = {};

$(document).ready(function () {
    $.get({
        url: '/get_data/',
        success: function (point) {
            data = point;
        },
    });
    chart = chartfunc();

    return data;
});


function chartfunc(){
    chart = Highcharts.chart('container', {
        chart: {
            defaultSeriesType: 'spline'

        },
        title: {
            text: 'Realtime ProcessTime data'
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
                text: 'ProcessTime',
                margin: 80
            }
        },
        series: [{
            name: 'OP10',
            data: []
        },{
            name: 'OP20',
            data: []
        },{
            name: 'OP30',
            data: []
        },{
            name: 'OP40',
            data: []
        },{
            name: 'OP50',
            data: []
        },{
            name: 'OP60',
            data: []
        }]
    });
    return chart;
}


$('#button').click(function () {
    var req_data = data;
 // For specific parameters, please see: https://api.hcharts.cn/highcharts#Series.addPoint
    var index=0;
    var handler = setInterval(function() {funt();},10000);
    function funt() {
        if(index<req_data['OP10'].length){
        index ++;
        if(index>=req_data['OP10'].length){
        ClearInterval(handler); //Close timing
        }
        shift = index > 20;
        chart.series[0].addPoint(req_data['OP10'][index], true, shift);
        chart.series[1].addPoint(req_data['OP20'][index], true, shift);
        chart.series[2].addPoint(req_data['OP30'][index], true, shift);
        chart.series[3].addPoint(req_data['OP40'][index], true, shift);
        chart.series[4].addPoint(req_data['OP50'][index], true, shift);
        chart.series[5].addPoint(req_data['OP60'][index], true, shift);
    }
    }
});