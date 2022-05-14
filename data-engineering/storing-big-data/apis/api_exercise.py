"""

    EXPLORE Data Science Academy
    © Explore Data Science Academy

    Storing Big Data - Retrieving Data: Part 1

    Practical Exercise

    Description: 
    Follow the code and instructions given below in order to complete this 
    API data retrieval exercise.   

"""

# We first import the packages needed to make an API call.
# We encourage you to explore the documentation for these libraries 
# further to understand their use within this script. 
import json # <-- Used to parse the JSON files we receive from the API
import urllib.request # <-- Used to call the AccuWeather API.

# =============================================================
# Fill in your details required to run the script 
API_KEY = "CnTfg7gCgCTorxXyq0etbg2otA0efZmH" # <-- Obtained from your AccuWeather App
LOCATION_ID = "252556" # <-- Obtained from the AccuWeather website
# =============================================================

# Here we create a function that takes in our credentials and
# location ID to make the request using `urllib`.
def get_weather(api_key, location_id):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    print(data)
    return (data[0]['Temperature']['Imperial']['Value'],
            data[0]['RelativeHumidity'],
            data[0]['Wind']['Direction']['Degrees'],
            data[0]['Wind']['Speed']['Imperial']['Value'],
            data[0]['UVIndex'],
            data[0]['CloudCover'],
            data[0]['Pressure']['Metric']['Value'],
            data[0]['Precip1hr']['Metric']['Value'],
            data)


timestamp = time.time()

temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw \
    = get_weather(API, LOCATION_ID)

    """Retrieves the current weather conditions for a specified geographic 
       location using the AccuWeather API.  

    Args:
        api_key (string): Alphanumeric string representing a secret API key issued by AccuWeather.
        location_id (string): Six-digit number representing the location for which weather conditions will be collected.

    Returns:
        json object: Current weather conditions for the specified location.
    """

    # We format our URL in order to retrieve the current weather conditions for our desired location. This url is based off the Accuweather API documentation: 
    # https://developer.accuweather.com/accuweather-current-conditions-api/apis
    
    URL = f'http://dataservice.accuweather.com/currentconditions/v1/{location_id}?apikey={api_key}&details=true'

    try: 
        print(f'Calling the AccuWeather API with the following URL: {URL}')
        
        # Use urllib to perform a GET request to the API using our formatted URL.
        with urllib.request.urlopen(URL) as url:
            # Load and decode the resulting JSON data received from the API.
            data = json.loads(url.read().decode())
    except Exception as e: 
        print (f"Something went wrong in contacting the API service.\
               The following exception was obtained:{e}")
        data = None
    return data

def parse_accuweather_data(json_data):
    """Function to extract specific fields from the received
       AccuWeather response.  

    Args:
        json_data (json object): The JSON data payload received from the AccuWeather API
    """

    # =============================================================
    #                      Challenge Yourself
    # 
    # Once you have successfully run the basic script, try and extract
    # specific elements that you are intereseted in, and use this 
    # function to display them. For example, you could try and extract 
    # the Temperature or the RealFeelTemperature values from the 
    # AccuWeather data payload.
    # =============================================================

    print ("*** The functionality to parse the received JSON data has not been implemented yet. Please do so! ***")

def main():
    response = get_weather(API_KEY, LOCATION_ID)
    if response is not None:
        print ("***API Call Successful! The Following data was received*** \n")
        print(response)
        print ("\n")
        parse_accuweather_data(response)
        print ("\n")

if __name__ == "__main__":
    main()
