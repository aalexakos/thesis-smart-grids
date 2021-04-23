import requests
import common

response = requests.get(
    f'https://api.tomorrow.io/v4/timelines?location={common._lat}%2C{common._lon}&fields={common._fields}&timesteps=1h&apikey={common._key}')
data_response = response.json()

timeline = data_response['data']['timelines'][0]
print('timestep', timeline['timestep'])
print('startTime', timeline['startTime'])
print('endTime', timeline['endTime'])
for interval in timeline['intervals']:
    print(interval)
