import requests

def make_api_request(url, params):	
	try:
		response = requests.get(url, params=params)
		response.raise_for_status()
		return response.json()

	except requests.exceptions.HTTPError as http_err:
		print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
  
	except Exception as err:
		print(f"An error occurred: {err}")
  
		
	return None