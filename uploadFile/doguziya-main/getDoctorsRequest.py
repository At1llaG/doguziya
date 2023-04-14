import requests
import json

apiUrl = 'https://www.hastanemyanimda.com/api/users'
response = requests.get(apiUrl)

if response.status_code == 200:
    data = response.json()
    with open('doctors.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data successfully written to doctors.json')
else:
    print('An error occurred while fetching data from the API')
