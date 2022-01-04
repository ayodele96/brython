from browser import window

b_highchart = window.Highcharts.Chart.new

b_highchart({        
    'chart': {
        'plotBackgroundColor': '#FCFFC5',
        'plotBorderWidth': None,
        'plotShadow': False,
        'renderTo': 'container'
    },
    'title': {
        'text': 'Religious Distribution in Nigeria'
    },
    'tooltip': {
        'pointFormat': '<b>{point.percentage:.1f}%</b>'
    },
    'plotOptions': {
        'pie': {
            'allowPointSelect': True,
            'cursor': 'pointer',
            'dataLabels': {
                'enabled': True,
                'format': '<b>{point.name}</b>: {point.percentage:.1f} %',
                'style': {
                    'color': 'black'
                }
            }
        }
    },
    'series': [{
        'type': 'pie',
        'data': [
            ['Indigenious Beliefs',   10.7],
            ['Other Christian',       35.3],
            {
                'name': 'Roman Catholicism',
                'y': 10.0,
                'sliced': True,
                'selected': True
            },
            ['Islam',    43.5],
            ['Others',     0.5]
        ]
    }]
})