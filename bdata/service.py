import requests

idd='qPTUpCLA'

endpoint=f'https://chalo.com/app/api/scheduler_v4/v4/mumbai/routedetailslive?route_id={idd}&day=thursday'

response=requests.get(endpoint)
# r=response.json()['route']['stopSequenceWithDetails'][]
lis=[]
for i in range(len(response.json()['route']['stopSequenceWithDetails'])):
    lis.append(response.json()['route']['stopSequenceWithDetails'][i]['stop_name'])
    lis.append(response.json()['route']['stopSequenceWithDetails'][i]['stop_lat'])
    lis.append(response.json()['route']['stopSequenceWithDetails'][i]['stop_lon'])

