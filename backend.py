import requests

API_KEY = "98bee7fd2b1c09247c4a71f303024f4b"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[nr_values]
    return filtered_data

if __name__== "__main__":
    print(get_data(place="Tokyo", forecast_days=3,))
