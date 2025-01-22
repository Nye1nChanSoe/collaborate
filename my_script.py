import requests

# URL to fetch data from
url = "https://api.github.com"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful!")
    # Print the JSON response
    print("Response Data:", response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
