from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/results', methods=["POST"])
def results():
    api_key = '219ee2cd1c341d93688001529dc36a06'
    city = request.form.get('city')
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + api_key
    print(url)
    response = requests.get(url).json()
    weather_list = response.get("list", [])
    first_weather_dict = weather_list[0]
    description = first_weather_dict.get("weather", [{}])[0].get("description")
    location = response.get('city', {}).get('name')
    country = response.get('city', {}).get('country')
    timezone = response.get('city', {}).get('timezone')
    timestamp = first_weather_dict.get('dt')
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    timestamp_local = datetime.fromtimestamp(timestamp)
    temp_k = first_weather_dict.get("main", {}).get("temp")
    temp_c = str(round(float(temp_k - 273.15), 2))
    wind_speed = first_weather_dict.get("wind", {}).get("speed")
    icon = first_weather_dict.get("weather", [{}])[0].get("icon")



    return render_template('results.html', tomorrow_weather=tomorrow_weather, description=description, location=location,
                           timezone=timezone, timestamp=timestamp, temp_c=temp_c, wind_speed=wind_speed, icon=icon,
                           country=country, date=date, temp_tommorow=temp_tommorow)


if __name__ == '__main__':
    app.run(debug=True)
