from operator import itemgetter
import requests

url = "https://bdapis.com/api/v1.1/division/rangpur"
r = requests.get(url).json()

# print(r['data'])

for district in r['data']:
    print(district['district'])
    print(district['upazilla'])
    
# see here: https://rapidapi.com/AbmSourav/api/bdapi and here: https://bdapis.com/ for more
