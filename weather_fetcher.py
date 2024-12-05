import requests
import json

API_KEY = "insert your API_KEY here"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    try:
        city = city.strip()
        response = requests.get(
            f"{BASE_URL}?key={API_KEY}&q={city}"
        )
        response.raise_for_status()
        data = json.loads(response.content)
        return data
    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the WeatherAPI. Please check your internet connection.")
        return None
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None
def process_data(data):
    try:
        city = data['location']['name']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        return city, country, temperature, condition, humidity
    except KeyError:
        print("Error processing data. Please verify the city name or try again.")
        return None

def show_weather(data):
    print("\n===Current Local Weather===")
    print(f"City: {data[0]}")
    print(f"Country: {data[1]}")
    print(f"Temperature: {data[2]}ºC")
    print(f"Condition: {data[3]}")
    print(f"Humidity: {data[4]}%\n")

def main():
    while True:
        city = input("Enter the name of the city (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Closing program.")
            break
        data = get_weather(city)
        if data:
            weather = process_data(data)
            if weather:
                show_weather(weather)
            else:
                print("Unable to retrieve weather information for the provided city.")
        else:
            print("City not found or connection error. Please verify the entered name")

if __name__ == '__main__':
    main()
