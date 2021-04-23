import datetime

import requests
import common

now = datetime.datetime.now()
endTime = now.strftime("%Y-%m-%dT%H:%M:%SZ")
past = now - datetime.timedelta(hours=5)
startTime = past.strftime("%Y-%m-%dT%H:%M:%SZ")

# this api call returns data only 6 hours in the past at max!
response = requests.get(
    f'https://api.tomorrow.io/v4/timelines?location={common._lat}%2C{common._lon}&fields={common._fields}&timesteps=1h&startTime={startTime}&endTime={endTime}&apikey={common._key}')
data_response = response.json()
print(response.json())

timeline = data_response['data']['timelines'][0]
print('timestep', timeline['timestep'])
print('startTime', timeline['startTime'])
print('endTime', timeline['endTime'])
for interval in timeline['intervals']:
    print(interval)
