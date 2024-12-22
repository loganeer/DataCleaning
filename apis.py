import requests
import pandas as pd

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
response = requests.get(url)
if response.status_code == 200:
    # Extract the response JSON data
    data = response.json()
    # Check if the API response contains cocktails data
    if 'drinks' in data:
        # Create DataFrame from drinks data
        df = pd.DataFrame(data['drinks'])
        # Print the resulting DataFrame
        print(df.head())
    else:
        print("No drinks found.")
else:
    print(f"Failed to retrieve data from API. Status code: {response.status_code}")
print(response.content)