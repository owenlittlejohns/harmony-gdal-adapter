def s1_info():
    s1 = [
  #Query 1
        {
        'q_num':'1',
        'reference_image':'grfn_query1_reference.tiff',
        'request_url':'science%2Fgrids%2Fdata%2Famplitude/coverage/rangeset?subset=lat(33:33.1)&subset=lon(-115.5:-115.25)&format=image%2Ftiff&granuleID=',
        'prod_gid':'G1715962900-ASF',
        'uat_gid':'G1234646236-ASF',
        'sit_gid':'G1234646236-ASF',
        'outfile':'_grfn_query1.tiff',
        'message':'Variable subset amplitude and spatial subset.',
        'cs': 'Geographic',
        'proj_cs':'NA',
        'gcs': 'WGS 84',
        'authority': 'EPSG',
        'proj_epsg': 'NA',
        'gcs_epsg': '4326',
        'subset': [33.0, 33.1, -115.5, -115.25],
        'bands': 1,
        'variables': ['amplitude', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'],
        'xy_size':[300, 120]
        },
#Query  2
       {
       'q_num':'2',
       'reference_image':'grfn_query2_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Fcoherence/coverage/rangeset?subset=lat(26.95:27.25)&subset=lon(37.25:38.15)&format=image%2Ftiff&granuleID=',
       'message':'Variable subset coherence and spatial subset.',
       'outfile':'_grfn_query2.tiff',
       'prod_gid':'G1944514838-ASF',
       'uat_gid':'G1235283005-ASF',
       'sit_gid':'G1235283005-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [26.95, 27.25, 37.25, 38.15],
       'bands': 1,
       'variables': ['coherence', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[1080, 360]
       },
#Query 3
       {
      'q_num':'3',
      'reference_image':'grfn_query3_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2FconnectedComponents/coverage/rangeset?subset=lat(27.0:27.5)&subset=lon(37.5:38.25)&format=image%2Ftiff&granuleID=',
       'message':'Variable subset connectedComponents. Spatial subset.',
       'outfile':'_grfn_query3.tiff',
       'prod_gid':'G1944514838-ASF',
       'uat_gid':'G1235283005-ASF',
       'sit_gid':'G1235283005-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [27.0, 27.5, 37.5, 38.25],
       'bands': 1,
       'variables': ['connectedComponents', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[900, 600]
       },
#Query 4
       {
       'q_num':'4',
       'reference_image':'grfn_query4_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2FunwrappedPhase/coverage/rangeset?subset=lat(26.9:27.5)&subset=lon(36.9:39.1)&format=image%2Ftiff&granuleID=',
       'message':'Variable subset unwrappedPhase and spatial subset',
       'outfile':'_grfn_query4.tiff',
       'prod_gid':'G1944514838-ASF',
       'uat_gid':'G1235283005-ASF',
       'sit_gid':'G1235283005-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [26.9, 27.5, 36.9, 39.1],
       'bands': 1,
       'variables': ['unwrappedPhase', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[2640, 720]
       },
#Query 5
       {
       'q_num':'5',
       'reference_image':'grfn_query5_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Famplitude%2Cscience%2Fgrids%2Fdata%2Fcoherence/coverage/rangeset?subset=lat(33:33.1)&subset=lon(-115.5:-115.25)&height=60&width=150&format=image%2Ftiff&granuleID=',
       'message':'Variable subset 2 variables (amplitude and coherence). Spatial subset and specify height and width of output.',
       'outfile':'_grfn_query5.tiff',
       'prod_gid':'G1715962900-ASF',
       'uat_gid':'G1234646236-ASF',
       'sit_gid':'G1234646236-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [33.0, 33.1, -115.5, -115.25],
       'bands': 2,
       'variables': ['amplitude', 'coherence', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[150, 60]
        },
#Query 6
       {
       'q_num':'6',
       'reference_image':'grfn_query6_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Famplitude%2Cscience%2Fgrids%2Fdata%2Fcoherence%2Cscience%2Fgrids%2Fdata%2FconnectedComponents/coverage/rangeset?subset=lat(33.05:33.1)&subset=lon(-115.52:-115.27)&height=30&width=75&format=image%2Ftiff&granuleID=',
       'message':'Varable subset 3 variables (amplitude, coherence, and connectedComponents). Specify height and width of output.',
       'outfile':'_grfn_query6.tiff',
       'prod_gid':'G1715962900-ASF',
       'uat_gid':'G1234646236-ASF',
       'sit_gid':'G1234646236-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [33.05, 33.1, -115.52, -115.27],
       'bands': 3,
       'variables': ['amplitude', 'coherence', 'connectedComponents', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[75,30]
       },
#Query 7
       {
       'q_num':'7',
       'reference_image':'grfn_query7_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Famplitude%2Cscience%2Fgrids%2Fdata%2Fcoherence%2Cscience%2Fgrids%2Fdata%2FconnectedComponents%2Cscience%2Fgrids%2Fdata%2FunwrappedPhase/coverage/rangeset?subset=lat(32.95:33.09)&subset=lon(-115.45:-115.15)&format=image%2Ftiff&granuleID=',
       'message':'Variable subset 4 variables with comma separated list. Spatial subset.',
       'outfile':'_grfn_query7.tiff',
       'prod_gid':'G1715962900-ASF',
       'uat_gid':'G1234646236-ASF',
       'sit_gid':'G1234646236-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [32.95, 33.09, -115.45, -115.15],
       'bands': 4,
       'variables': ['amplitude', 'coherence', 'connectedComponents', 'unwrappedPhase', 'NA', 'NA', 'NA'],
       'xy_size':[360,168]
       },
#Query 8: South America (negative lat and long) spatial subset area smaller than product bounding box
       {
       'q_num':'8',
       'reference_image':'grfn_query8_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Famplitude/coverage/rangeset?subset=lat(-37.2:-36.9)&subset=lon(-69.8:-68.8)&format=image%2Ftiff&granuleID=',
       'message':'Spatial subset in negative lat and lon region. Subset bbox smaller than original granule extent.',
       'outfile':'_grfn_query8.tiff',
       'prod_gid':'G1697222082-ASF',
       'uat_gid':'G1233786871-ASF',
       'sit_gid':'G1233786871-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [-37.2, -36.9, -69.8, -68.8],
       'bands': 1,
       'variables': ['amplitude', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[1200,360]
       },
#Query 9: South America (negative lat and long) spatial subset area larger than product bounding box
       {
       'q_num':'9',
       'reference_image':'grfn_query9_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Fcoherence/coverage/rangeset?subset=lat(-39.0:-35.0)&subset=lon(-71.6:-67.5)&format=image%2Ftiff&granuleID=',
       'message':'Spatial subset in negative lat and lon region. Subset bbox larger than original granule extent.',
       'outfile':'_grfn_query9.tiff',
       'prod_gid':'G1697222082-ASF',
       'uat_gid':'G1233786871-ASF',
       'sit_gid':'G1233786871-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [-38.14, -36.0, -71.41, -67.96],
       'bands': 1,
       'variables': ['coherence', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[4143,2559]
       },

#Query 10: China spatial subset area smaller than product bounding box
       {
       'q_num':'10',
       'reference_image':'grfn_query10_reference.tiff',
       'request_url':'science%2Fgrids%2Fdata%2Fcoherence%2Cscience%2Fgrids%2Fdata%2FunwrappedPhase/coverage/rangeset?subset=lat(43.75:44.85)&subset=lon(86.85:88.15)&format=image%2Ftiff&granuleID=',
       'message':'Variable subset coherence and unwrappedPhase. Spatial subset bbox totaly enclosed in original granule extent.',
       'outfile':'_grfn_query10.tiff',
       'prod_gid':'G1722540208-ASF',
       'uat_gid':'G1234873982-ASF',
       'sit_gid':'G1234873982-ASF',
       'cs': 'Geographic',
       'proj_cs':'NA',
       'gcs': 'WGS 84',
       'authority': 'EPSG',
       'proj_epsg': 'NA',
       'gcs_epsg': '4326',
       'subset': [43.75, 44.85, 86.85, 88.15],
       'bands': 2,
       'variables': ['coherence', 'unwrappedPhase', 'NA', 'NA', 'NA', 'NA', 'NA'],
       'xy_size':[1560,1320]
       },
#Query 11: Verify png output works
       {
       'q_num':'11',
       'request_url':'science%2Fgrids%2Fdata%2Famplitude/coverage/rangeset?subset=lat(33:33.05)&subset=lon(-115.5:-115.45)&format=image%2Fpng&granuleID=',
       'message':'This query specifies png output and the tests verify that the product file is png.',
       'outfile':'_grfn_query11',
       'prod_gid':'G1715962900-ASF',
       'uat_gid':'G1234646236-ASF',
       'sit_gid':'G1234646236-ASF',
       'file_type':'png'
       },
#Query 12: Verify gif output works
       {
       'q_num':'12',
       'request_url':'science%2Fgrids%2Fdata%2Famplitude/coverage/rangeset?subset=lat(33:33.05)&subset=lon(-115.5:-115.45)&format=image%2Fgif&granuleID=',
       'message':'This query specifies gif output and the tests verify that the product file is gif.',
       'outfile':'_grfn_query12',
       'prod_gid':'G1715962900-ASF',
       'uat_gid':'G1234646236-ASF',
       'sit_gid':'G1234646236-ASF',
       'file_type':'gif'
       }
         ]
    return s1
