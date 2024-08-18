# Weather App

# This line of code displays a welcome message to the user whenever the weather forecast app is run.
print("Welcome to our weather forecast app. We hope that you have a great experience using it.")

# The weather_data variable contains weather data for multiple cities in the form of a dictionary.
weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy",
"wind_speed": "5 km/h", "humidity": "80%"}, "New York": {"temperature":
"20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity":
"50%"}, "Tokyo": {"temperature": "18°C", "conditions": "Rainy",
"wind_speed": "7 km/h", "humidity": "90%"}, "Sydney": {"temperature":
"22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity":
"60%"}, "Paris": {"temperature": "17°C", "conditions": "Foggy",
"wind_speed": "3 km/h", "humidity": "85%"} }

# This line of code lets the user enter the name of the city they would like to know the weather data of.
city_name = input("Please enter the name of the city you would like to know the weather of today.")

# The following if statements allow the respective weather data for each city to display individually, based on the user's choice of city.
if city_name == "London":
    print(weather_data["London"])
elif city_name == "New York":
    print(weather_data["New York"])
elif city_name == "Tokyo":
    print(weather_data["Tokyo"])
elif city_name == "Sydney":
    print(weather_data["Sydney"])
elif city_name == "Paris":
    print(weather_data["Paris"])
else:
    print("You have entered an invalid city name.")

# Once the weather app has been used, a final message will display, thanking the user
print("Thank you for using our weather forecast. We hope that you use it again in the near future.")