import requests

def fetch_fire_data(api_key, date="2025-01-18"):
    """
    Fetch fire data from the NASA FIRMS API in CSV format.
    
    :param api_key: Your NASA FIRMS API key.
    :param date: The date of interest for the fire data (YYYY-MM-DD).
    :return: Raw CSV data as a string.
    """
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{api_key}/VIIRS_SNPP_NRT/world/1/{date}"
    
    response = requests.get(url)
    print("Status Code:", response.status_code)  # Debug: Check status.
    print("Response Headers:", response.headers)  # Debug: Check content type.

    if response.status_code == 200:
        if "text/plain" in response.headers["Content-Type"]:
            return response.text  # Raw CSV content.
        else:
            raise Exception("The response is not in CSV format.")
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
