def avnir_info():
    avnir = [
    # Query 1
    {
    'q_num':'1',
    'request_url':'Band1%2CBand2/coverage/rangeset?subset=lat(-.05:0.25)&subset=lon(-51.0:-50.75)&format=image%2Ftiff&granuleID=',
    'message':'Subset across the Equator. Variable subset bands 1 & 2',
    'prod_gid':'G1813212660-ASF',
    'uat_gid':'G1236469528-ASF',
    'sit_gid':'G1236469528-ASF',
    'outfile':'_avnir_query1.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 22N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32622',
    'gcs_epsg': '4326',
    # modified for mask 'subset': [-.05, .25, -51.0,-50.75],
    'subset': [-0.05, 0.3, -50.99, -50.75],
    'bands': 2,
    'variables': ['Band1', 'Band2', 'NA', 'NA'],
    'xy_size':[3410, 2660]
    },
    # Query 2
    {
    'q_num':'2',
    'request_url':'Band3%2CBand4/coverage/rangeset?subset=lat(14.8:14.9)&subset=lon(-0.15:0.15)&format=image%2Ftiff&granuleID=',
    'message':'Subset across prime meridian. Variable subset bands 3 & 4.',
    'prod_gid':'G1817336128-ASF',
    'uat_gid':'G1236469518-ASF',
    'sit_gid':'G1236469518-ASF',
    'outfile':'_avnir_query2.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 30N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32630',
    'gcs_epsg': '4326',
    # modified for mask 'subset': [14.8, 14.9, -0.15, 0.15],
    'subset': [14.74, 14.96, -0.14, 0.14],
    'bands': 2,
    'variables': ['Band3', 'Band4', 'NA', 'NA'],
    'xy_size':[3380, 494]
    },
    # Query 3
    {
    'q_num':'3',
    'request_url':'Band1%2CBand2/coverage/rangeset?subset=lat(66.5:66.75)&subset=lon(179.75:-179.85)&format=image%2Ftiff&granuleID=',
    'message':'Subset across the anti-meridian. ',
    'prod_gid':'G1835935580-ASF',
    'uat_gid':'G1236469523-ASF',
    'sit_gid':'G1236469523-ASF',
    'outfile':'_avnir_query3.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 1N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32601',
    'gcs_epsg': '4326',
    #modified for mask 'subset': [66.5, 66.75, 179.75, -179.85],
    'subset': [66.44, 66.81, 179.85, -179.95],
    'bands': 2,
    'variables': ['Band1', 'Band2', 'NA', 'NA'],
    'xy_size':[2868, 1638]
    },
    # Query 4
    {
    'q_num':'4',
    'request_url':'Band4/coverage/rangeset?subset=lat(36.9:37.1)&subset=lon(-99.15:-98.85)&format=image%2Ftiff&granuleID=',
    'message':'Northern Hemisphere spatial subset. Variable subset Band4',
    'prod_gid':'G1849288272-ASF',
    'uat_gid':'G1236469517-ASF',
    'sit_gid':'G1236469517-ASF',
    'outfile':'_avnir_query4.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 14N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32614',
    'gcs_epsg': '4326',
    #modified for mask 'subset': [36.9, 37.1, -99.15, -98.85],
    'subset': [36.85, 37.15, -99.13, -98.87],
    'bands': 1,
    'variables': ['Band4', 'NA', 'NA', 'NA'],
    'xy_size':[3109, 1545]
    },
    # Query 5
    {
    'q_num':'5',
    'request_url':'all/coverage/rangeset?subset=lat(36.95:37.05)&subset=lon(-99.2:-98.9)&format=image%2Ftiff&granuleID=',
    'message':'Northern Hemisphere spatial subset. Variable subset 4 bands using "all".',
    'prod_gid':'G1849288272-ASF',
    'uat_gid':'G1236469517-ASF',
    'sit_gid':'G1236469517-ASF',
    'outfile':'_avnir_query5.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 14N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32614',
    'gcs_epsg': '4326',
    #modified for mask 'subset': [36.95, 37.05, -99.2, -98.9],
    'subset': [36.9, 37.1, -99.18, -98.92],
    'bands': 4,
    'variables': ['Band1', 'Band2', 'Band3', 'Band4'],
    'xy_size':[2853, 463]
    },
    # Query 6
    {
    'q_num':'6',
    'request_url':'Band1%2CBand3/coverage/rangeset?subset=lat(-26.1:-25.8)&subset=lon(18.07:18.25)&format=image%2Ftiff&height=30&width=75&granuleID=',
    'message':'Southern Hemisphere spatial subset, variable subset bands 1 & 3 and specify xy_size',
    'prod_gid':'G1835549401-ASF',
    'uat_gid':'G1234864684-ASF',
    'sit_gid':'G1234864684-ASF',
    'outfile':'_avnir_query6.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 34S',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32734',
    'gcs_epsg': '4326',
    #modified for mask 'subset': [-26.1, -25.8, 18.07, 18.25],
    'subset': [-26.13, -25.77, 18.07, 18.25],
    'bands': 2,
    'variables': ['Band1', 'Band3', 'NA', 'NA'],
    'xy_size':[75, 30]
    },
    # Query 7
    {
    'q_num':'7',
    'request_url':'Band1%2CBand2%2CBand3%2CBand4/coverage/rangeset?subset=lat(49.65:49.95)&subset=lon(-97.65:-97.35)&format=image%2Ftiff&height=45&width=90&granuleID=',
    'message':'Negative longitude spatial subset, specify xy size and all bands with comma separated list',
    'prod_gid':'G1906378530-ASF',
    'uat_gid':'G1236469519-ASF',
    'sit_gid':'G1236469519-ASF',
    'outfile':'_avnir_query7.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 14N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32614',
    'gcs_epsg': '4326',
    #modified for mask 'subset': [49.65, 49.95, -97.65, -97.35],
    'subset': [49.6, 49.99, -97.64, -97.36],
    'bands': 4,
    'variables': ['Band1', 'Band2', 'Band3', 'Band4'],
    'xy_size':[90, 45]
    },
    # Query 8
    {
    'q_num':'8',
    'request_url':'all/coverage/rangeset?subset=lat(9.2:10.3)&subset=lon(-79.9:-78.9)&format=image%2Ftiff&granuleID=',
    'message':'Spatial subset larger than granule bounding box and "all" variables.',
    'prod_gid':'G1813329318-ASF',
    'uat_gid':'G1234864683-ASF',
    'sit_gid':'G1234864683-ASF',
    'outfile':'_avnir_query8.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 17N',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32617',
    'gcs_epsg': '4326',
    'subset': [9.4, 10.24, -79.7, -79.2],
    'bands': 4,
    'variables': ['Band1', 'Band2', 'Band3', 'Band4'],
    'xy_size':[7215, 8000]
    },
    # Query 9
    {
    'q_num':'9',
    'request_url':'all/coverage/rangeset?subset=lat(-26.1:-26.0)&subset=lon(18.4:18.6)&format=image%2Ftiff&subset=time(%222008-11-30T08%3A59%3A23Z%22%3A%222008-11-30T08%3A59%3A36Z%22)',
    'message':'Temporal search should only return one file in this temporal range. All variables and spatial subset.',
    'prod_gid':'',
    'uat_gid':'',
    'sit_gid':'',
    'outfile':'_avnir_query9.tiff',
    'cs': 'Projected',
    'proj_cs':'WGS 84 / UTM zone 34S',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': '32734',
    'gcs_epsg': '4326',
    # modified for mask 'subset': [-26.1, -26.0, 18.4, 18.6],
    'subset': [-26.13, -25.96, 18.41, 18.59],
    'bands': 4,
    'variables': ['Band1', 'Band2', 'Band3', 'Band4'],
    'xy_size':[2169, 732]
    },
    # Query 10
    {
    'q_num':'10',
    'request_url':'Band2/coverage/rangeset?subset=lat(-.05:0.25)&subset=lon(-51.0:-50.75)&format=image%2Fpng&granuleID=',
    'message':'Test to verify that png file output works and subset across equator.',
    'prod_gid':'G1813212660-ASF',
    'uat_gid':'G1236469528-ASF',
    'sit_gid':'G1236469528-ASF',
    'outfile':'_avnir_query10',
    'cs': 'Projected',
    'proj_cs':'',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [],
    'bands': 1,
    'variables': ['NA', 'NA', 'NA', 'NA'],
    'xy_size':[0, 0],
    'file_type':'png'
    },
    # Query 11
    {
    'q_num':'11',
    'request_url':'Band2/coverage/rangeset?subset=lat(-.05:0.25)&subset=lon(-51.0:-50.75)&format=image%2Fgif&granuleID=',
    'message':'Test to verify that gif file output works and subset across the Equator',
    'prod_gid':'G1813212660-ASF',
    'uat_gid':'G1236469528-ASF',
    'sit_gid':'G1236469528-ASF',
    'outfile':'_avnir_query11',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [],
    'bands': 1,
    'variables': ['NA', 'NA', 'NA', 'NA'],
    'xy_size':[0, 0],
    'file_type':'gif'
    }
    ]
    return avnir
