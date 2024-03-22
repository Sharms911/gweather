from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

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

    today_date = datetime.now().date()


    #today plus one temp
    datetodayplusone = today_date + timedelta(days=1)

    temptodayplusone = [forecast['main']['temp'] for forecast in response.get("list", [])
                        if datetime.fromtimestamp(forecast['dt']).date() == datetodayplusone]
    ttp1 = round(sum(temptodayplusone) / len(temptodayplusone) -273.1)


    #today plus 2 temp
    datetodayplustwo = today_date + timedelta(days=2)

    temptodayplustwo = [forecast['main']['temp'] for forecast in weather_list
                        if datetime.fromtimestamp(forecast['dt']).date() == datetodayplustwo]
    ttp2 = round(sum(temptodayplustwo) / len(temptodayplustwo) -273.1)

    # today plus 3 temperature
    datetodayplusthree = today_date + timedelta(days=3)

    temptodayplusthree = [forecast['main']['temp'] for forecast in weather_list
                        if datetime.fromtimestamp(forecast['dt']).date() == datetodayplusthree]
    ttp3 = round(sum(temptodayplusthree) / len(temptodayplusthree) - 273.1)

    # today plus 4 temp
    datetodayplusfour = today_date + timedelta(days=4)

    temptodayplusfour = [forecast['main']['temp'] for forecast in weather_list
                        if datetime.fromtimestamp(forecast['dt']).date() == datetodayplusfour]
    ttp4 = round(sum(temptodayplusfour) / len(temptodayplusfour) - 273.1)


    temptodayplustwo = [forecast['main']['temp'] for forecast in weather_list
                        if datetime.fromtimestamp(forecast['dt']).date() == datetodayplustwo]
    ttp2 = round(sum(temptodayplustwo) / len(temptodayplustwo) - 273.1)

    print(temptodayplusone)
    return render_template('results.html', ttp1=ttp1, ttp2=ttp2, ttp3=ttp3, ttp4=ttp4, today_date=today_date, description=description, location=location,
                           timezone=timezone, timestamp=timestamp, temp_c=temp_c, wind_speed=wind_speed, icon=icon,
                           country=country, date=date)


if __name__ == '__main__':
    app.run(debug=True)
