import requests

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=10)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("Status: 200 OK - Request successful!")
        
        data = response.json()
        print("\nJSON Output Keys:")
        for key in data.keys():
            print(f"- {key}")
    else:
        print(f"Received unexpected status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching data: {e}")