import requests

def work():
    base_url = "https://api.opendota.com/api/matches/"
    match_id = int(input("Введіть id гри: "))
    url = f"{base_url}{match_id}"
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    print(type(data))

work()    