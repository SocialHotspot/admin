// CHART SPLINE
// ----------------------------------- 
(function(window, document, $, undefined){

  $(function(){

    var data = [{
      "label": "Total likes",
      "color": "#768294",
      "data": [
        ["Mar", 70],
        ["Apr", 85],
        ["May", 59],
        ["Jun", 93],
        ["Jul", 66],
        ["Aug", 86],
        ["Sep", 60]
      ]
    }, {
      "label": "Social Hotspot",
      "color": "#1f92fe",
      "data": [
        ["Mar", 21],
        ["Apr", 12],
        ["May", 27],
        ["Jun", 24],
        ["Jul", 16],
        ["Aug", 39],
        ["Sep", 15]
      ]
    }];

    var datav2 = [{
      "label": "Total check-ins",
      "color": "#768294",
      "data": [
	    ["Mar", 86],
	    ["Apr", 60],
        ["May", 59],
        ["Jun", 93],
        ["Jul", 66],
        ["Aug", 85],
        ["Sep", 70]
      ]
    }, {
      "label": "Social Hotspot",
      "color": "#7266ba",
      "data": [
        ["Mar", 21],
        ["Apr", 24],
        ["May", 16],
        ["Jun", 39],
        ["Jul", 15],
        ["Aug", 21],
        ["Sep", 12]
      ]
    }];

    /* var datav3 = [{
      "label": "Home",
      "color": "#1ba3cd",
      "data": [
        ["1", 38],
        ["2", 40],
        ["3", 42],
        ["4", 48],
        ["5", 50],
        ["6", 70],
        ["7", 145],
        ["8", 70],
        ["9", 59],
        ["10", 48],
        ["11", 38],
        ["12", 29],
        ["13", 30],
        ["14", 22],
        ["15", 28]
      ]
    }, {
      "label": "Overall",
      "color": "#3a3f51",
      "data": [
        ["1", 16],
        ["2", 18],
        ["3", 17],
        ["4", 16],
        ["5", 30],
        ["6", 110],
        ["7", 19],
        ["8", 18],
        ["9", 110],
        ["10", 19],
        ["11", 16],
        ["12", 10],
        ["13", 20],
        ["14", 10],
        ["15", 20]
      ]
    }]; */

    var options = {
      series: {
          lines: {
              show: false
          },
          points: {
              show: true,
              radius: 4
          },
          splines: {
              show: true,
              tension: 0.4,
              lineWidth: 1,
              fill: 0.5
          }
      },
      grid: {
          borderColor: '#eee',
          borderWidth: 1,
          hoverable: true,
          backgroundColor: '#fcfcfc'
      },
      tooltip: true,
      tooltipOpts: {
          content: function (label, x, y) { return x + ' : ' + y; }
      },
      xaxis: {
          tickColor: '#fcfcfc',
          mode: 'categories'
      },
      yaxis: {
          min: 0,
          max: 150, // optional: use it for a clear represetation
          tickColor: '#eee',
          //position: 'right' or 'left',
          tickFormatter: function (v) {
              return v/* + ' visitors'*/;
          }
      },
      shadowSize: 0
    };

    var chart = $('.chart-spline');
    $.plot(chart, data, options);
    
    var chartv2 = $('.chart-spline-2');
    $.plot(chartv2, datav2, options);

  });

})(window, document, window.jQuery);