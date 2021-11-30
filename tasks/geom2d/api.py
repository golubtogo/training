import requests

# response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
response = requests.get('https://www.cbr-xml-daily.ru/daily.xml')
print(response)
