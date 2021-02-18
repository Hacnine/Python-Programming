import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=4))

# print(len(data['list']['resource'])) will print that how many resource there.For details
# watch this video ' Python Tutorial: Working with JSON Data using the json Module '

usd_rates = dict()
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
#   print(name, price)
    usd_rates[name] = price

#  print(usd_rates["USD/EUR"])

print(50 * float(usd_rates['USD/INR']))
