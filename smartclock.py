from time import strftime
from tkinter import *
from datetime import *
from dotenv import load_dotenv
import os
import requests, json 
import calendar 
from PIL import ImageTk, Image
import pendulum


load_dotenv()

#Getting API key from ENV file
api_key = os.getenv('API')

#Grabbing current weather and forecasat data
url_current = 'http://dataservice.accuweather.com/currentconditions/v1/47173?apikey=' + api_key
url_forecast = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/47173?apikey=' + api_key + '&metric=true'



response_current = requests.get(url_current) 
response_forecast = requests.get(url_forecast)

#checking HTTP response, filling in with dummy data if it's not 200
if response_current == 200 or response_forecast == 200:
    print('good')
    current_json = response_current.json()
    forecast_json = response_forecast.json()    

else:
    print('Bad')
    current_json = [
            {
                "LocalObservationDateTime": "2021-02-24T16:18:00-08:00",
                "EpochTime": 1614212280,
                "WeatherText": "Cloudy",
                "WeatherIcon": 1,
                "HasPrecipitation": False,
                "PrecipitationType": True,
                "IsDayTime": True,
                "Temperature": {
                "Metric": {
                    "Value": 0.0,
                    "Unit": "C",
                    "UnitType": 17
                },
                "Imperial": {
                    "Value": 43,
                    "Unit": "F",
                    "UnitType": 18
                }
                },
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/current-weather/47173?lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/current-weather/47173?lang=en-us"
            }
        ]
    forecast_json = {
        "Headline": {
            "EffectiveDate": "2021-02-24T19:00:00-08:00",
            "EffectiveEpochDate": 1614222000,
            "Severity": 5,
            "Text": "Rain tonight",
            "Category": "rain",
            "EndDate": "2021-02-25T07:00:00-08:00",
            "EndEpochDate": 1614265200,
            "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/extended-weather-forecast/47173?unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?unit=c&lang=en-us"
        },
        "DailyForecasts": [
            {
            "Date": "2021-02-24T07:00:00-08:00",
            "EpochDate": 1614178800,
            "Temperature": {
                "Minimum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                },
                "Maximum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                }
            },
            "Day": {
                "Icon": 1,
                "IconPhrase": "Mostly cloudy",
                "HasPrecipitation": False
            },
            "Night": {
                "Icon": 1,
                "IconPhrase": "Rain",
                "HasPrecipitation": True,
                "PrecipitationType": "Rain",
                "PrecipitationIntensity": "Light"
            },
            "Sources": [
                "AccuWeather"
            ],
            "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=1&unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=1&unit=c&lang=en-us"
            },
            {
            "Date": "2021-02-25T07:00:00-08:00",
            "EpochDate": 1614265200,
            "Temperature": {
                "Minimum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                },
                "Maximum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                }
            },
            "Day": {
                "Icon": 1,
                "IconPhrase": "Intermittent clouds",
                "HasPrecipitation": False
            },
            "Night": {
                "Icon": 1,
                "IconPhrase": "Partly cloudy",
                "HasPrecipitation": False
            },
            "Sources": [
                "AccuWeather"
            ],
            "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=2&unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=2&unit=c&lang=en-us"
            },
            {
            "Date": "2021-02-26T07:00:00-08:00",
            "EpochDate": 1614351600,
            "Temperature": {
                "Minimum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                },
                "Maximum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                }
            },
            "Day": {
                "Icon": 1,
                "IconPhrase": "Mostly sunny",
                "HasPrecipitation": False
            },
            "Night": {
                "Icon": 1,
                "IconPhrase": "Mostly clear",
                "HasPrecipitation": False
            },
            "Sources": [
                "AccuWeather"
            ],
            "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=3&unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=3&unit=c&lang=en-us"
            },
            {
            "Date": "2021-02-27T07:00:00-08:00",
            "EpochDate": 1614438000,
            "Temperature": {
                "Minimum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                },
                "Maximum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                }
            },
            "Day": {
                "Icon": 1,
                "IconPhrase": "Mostly cloudy",
                "HasPrecipitation": False
            },
            "Night": {
                "Icon": 1,
                "IconPhrase": "Showers",
                "HasPrecipitation": True,
                "PrecipitationType": "Rain",
                "PrecipitationIntensity": "Light"
            },
            "Sources": [
                "AccuWeather"
            ],
            "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=4&unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=4&unit=c&lang=en-us"
            },
            {
            "Date": "2021-02-28T07:00:00-08:00",
            "EpochDate": 1614524400,
            "Temperature": {
                "Minimum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                },
                "Maximum": {
                "Value": 0.0,
                "Unit": "C",
                "UnitType": 17
                }
            },
            "Day": {
                "Icon": 1,
                "IconPhrase": "Rain",
                "HasPrecipitation": True,
                "PrecipitationType": "Rain",
                "PrecipitationIntensity": "Light"
            },
            "Night": {
                "Icon": 1,
                "IconPhrase": "Rain",
                "HasPrecipitation": True,
                "PrecipitationType": "Rain",
                "PrecipitationIntensity": "Light"
            },
            "Sources": [
                "AccuWeather"
            ],
            "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=5&unit=c&lang=en-us",
            "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=5&unit=c&lang=en-us"
            }
        ]
        }


response_sunrise_sunset = requests.get('https://api.sunrise-sunset.org/json?lat=49.166592&lng=-123.133568&formatted=0')

sunrise_sunset_json = response_sunrise_sunset.json()

current_temperature = current_json[0]['Temperature']['Metric']['Value']
current_weather = current_json[0]['WeatherText']
current_weather_icon_num = str(current_json[0]['WeatherIcon'])

#Creating weekday abbreviations
weekDays = ("M ","Tu","W ","Th","F ","Sa","Su")

#Getting sunrise time from API and formatting it into string
sunrise = sunrise_sunset_json['results']['sunrise']
sunrise_utc = pendulum.parse(sunrise, tz='UTC')
sunrise_pst = sunrise_utc.in_timezone("US/Pacific")
sunrise_pst_str = sunrise_pst.format('h:mm A')

#Getting sunset time from API and foramtting it into string
sunset = sunrise_sunset_json['results']['sunset']
sunset_utc = pendulum.parse(sunset, tz='UTC')
sunset_pst = sunset_utc.in_timezone("US/Pacific")
sunset_pst_str = sunset_pst.format('h:mm A')

#Getting today's date
today_date = date.today()

#Creating empty dictionaries for icons and forecast
icons = {}
forecast = {}

#creating forecast within forecast dictionary for the 5 day forecast
for i in range(0,5):
    forecast['day_of_week' + str(i)] = weekDays[(date.today()+ timedelta(i)).weekday()]
    forecast['temp_low' + str(i)] = str(forecast_json['DailyForecasts'][i]['Temperature']['Minimum']['Value'])
    forecast['temp_high' + str(i)] = str(forecast_json['DailyForecasts'][i]['Temperature']['Maximum']['Value'])
    forecast['icon_day' + str(i)] = str(forecast_json['DailyForecasts'][i]['Day']['Icon'])
    forecast['icon_night' + str(i)] = str(forecast_json['DailyForecasts'][i]['Night']['Icon'])

#Begin create GUI
root = Tk()
root.geometry("500x480")
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=0)

#Populating dictionary for icon files
for i in range(1,45):
    if i not in [9, 10, 27, 28]:
        icons[str(i)] = ImageTk.PhotoImage(Image.open('icons/' + str(i) + '.png'))


current_weather_icon = ImageTk.PhotoImage(Image.open('icons/' + current_weather_icon_num + '.png'))

#Updating time label
def update_time():
    current_time = strftime('%I:%M:%S %p')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_time)
#Updating date label
def update_date():
    current_date = today_date.strftime("%d-%b-%Y")
    lbl_date.configure(text = current_date)
    lbl_date.after(80, update_date)

#Updating day label
def update_day():
    current_day = today_date.strftime("%A")
    lbl_day.configure(text = current_day)
    lbl_day.after(80, update_date)  

frm_datetime = Frame(root)
frm_datetime.grid(row=0, column=0, sticky='w')

clock_label = Label(frm_datetime, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.grid(row=0, column=0, sticky='w')

lbl_date = Label(frm_datetime, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
lbl_date.grid(column = 0, row= 1)

lbl_day = Label(frm_datetime, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
lbl_day.grid(column = 0, row= 2)

frm_weather = Frame(root)
frm_weather.grid(row=0, column=2, sticky=NW)

lbl_weather_current = Label(frm_weather, text= 'NAO: ' + str(current_temperature), bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_current.grid(row=0,column=0, sticky=NW)

lbl_weather_current_img = Label(frm_weather, image = current_weather_icon)
lbl_weather_current_img.grid(row=0,column=1, sticky=NW)

lbl_weather0 = Label(frm_weather, text= forecast['day_of_week0'] + '= High: ' + forecast['temp_high0'] + ' Low: ' + forecast['temp_low0'], bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather0.grid(row=1,column=0, sticky=NW)

lbl_weather_day_0_img = Label(frm_weather, image = icons[forecast['icon_day0']])
lbl_weather_day_0_img.grid(row=1,column=1, sticky=NW)

lbl_weather_night_0_img = Label(frm_weather, image = icons[forecast['icon_night0']])
lbl_weather_night_0_img.grid(row=1,column=2, sticky=NW)

lbl_weather1 = Label(frm_weather, text= forecast['day_of_week1'] + '= High: ' + forecast['temp_high1'] + ' Low: ' + forecast['temp_low1'], bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather1.grid(row=2,column=0, sticky=NW)

lbl_weather_day_1_img = Label(frm_weather, image = icons[forecast['icon_day1']])
lbl_weather_day_1_img.grid(row=2,column=1, sticky=NW)

lbl_weather_night_1_img = Label(frm_weather, image = icons[forecast['icon_night1']])
lbl_weather_night_1_img.grid(row=2,column=2, sticky=NW)

lbl_weather2 = Label(frm_weather, text= forecast['day_of_week2'] + '= High: ' + forecast['temp_high2'] + ' Low: ' + forecast['temp_low2'], bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather2.grid(row=3,column=0, sticky=NW)

lbl_weather_day_2_img = Label(frm_weather, image = icons[forecast['icon_day2']])
lbl_weather_day_2_img.grid(row=3,column=1, sticky=NW)

lbl_weather_night_2_img = Label(frm_weather, image = icons[forecast['icon_night2']])
lbl_weather_night_2_img.grid(row=3,column=2, sticky=NW)

lbl_weather3 = Label(frm_weather, text= forecast['day_of_week3'] + '= High: ' + forecast['temp_high3'] + ' Low: ' + forecast['temp_low3'], bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather3.grid(row=4,column=0, sticky=NW)

lbl_weather_day_1_img = Label(frm_weather, image = icons[forecast['icon_day3']])
lbl_weather_day_1_img.grid(row=4,column=1, sticky=NW)

lbl_weather_night_1_img = Label(frm_weather, image = icons[forecast['icon_night3']])
lbl_weather_night_1_img.grid(row=4,column=2, sticky=NW)

lbl_weather4 = Label(frm_weather, text= forecast['day_of_week4'] + '= High: ' + forecast['temp_high4'] + ' Low: ' + forecast['temp_low4'], bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather4.grid(row=5,column=0, sticky=NW)

lbl_weather_day_4_img = Label(frm_weather, image = icons[forecast['icon_day4']])
lbl_weather_day_4_img.grid(row=5,column=1, sticky=NW)

lbl_weather_night_4_img = Label(frm_weather, image = icons[forecast['icon_night4']])
lbl_weather_night_4_img.grid(row=5,column=2, sticky=NW)

#Sunrise/Sunset frame

frm_sunrise_sunset = Frame(root)
frm_sunrise_sunset.grid(row=1, column=0, sticky='w')

lbl_sunrise = Label(frm_sunrise_sunset, text= 'Sunrise: ' + sunrise_pst_str)
lbl_sunrise.grid(row=0 ,column=0, sticky=NW)

lbl_sunset = Label(frm_sunrise_sunset, text= 'Sunset: ' + sunset_pst_str)
lbl_sunset.grid(row=1 ,column=0, sticky=NW)

frm_screenblank = Frame(root)
frm_screenblank.grid(row=2, column=0, sticky='w')

#Button to turn screenblank to 1 h 30 m

btn_screen_on = Button(frm_screenblank, text="Screen On", command=lambda: os.system("xset dpms 7800 7800 7800"))
btn_screen_on.grid(row=0, column=0, sticky='w')

#Button to turn screenblank to 30 seconds

btn_screen_off = Button(frm_screenblank, text="Screen Off", command=lambda: os.system("xset dpms 30 30 30"))
btn_screen_off.grid(row=0, column=1, sticky='w')

#updating date, time, and day
update_time()
update_date()
update_day()


root.mainloop()


