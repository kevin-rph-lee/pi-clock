from time import strftime
from tkinter import *
from datetime import *
from dotenv import load_dotenv
import os
import requests, json 
import calendar 
from PIL import ImageTk, Image


load_dotenv()

#Getting API key from ENV file
api_key = os.getenv('API')

#Grabbing current weather and forecasat data
url_current = 'http://dataservice.accuweather.com/currentconditions/v1/47173?apikey=' + api_key
url_forecast = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/47173?apikey=' + api_key + '&metric=true'
response_current = requests.get(url_current) 
response_forecast = requests.get(url_forecast) 
current_json = response_current.json()
forecast_json = response_forecast.json() 
current_temperature = current_json[0]['Temperature']['Metric']['Value']

#Creating weekday abbreviations
weekDays = ("M ","Tu","W ","Th","F ","Sa","Su")

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
root.geometry("480x320")
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=0)

#Populating dictionary for icon files
for i in range(1,45):
    if i not in [9, 10, 27, 28]:
        icons[str(i)] = ImageTk.PhotoImage(Image.open('icons/' + str(i) + '.png'))

#Updating time label
def update_time():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_time)
#Updating date label
def update_date():
    current_date = today_date.strftime("%d-%b-%Y")
    lbl_date.configure(text = current_date)
    lbl_date.after(80, update_date)

frm_datetime = Frame(root)
frm_datetime.grid(row=0, column=0, sticky='w')

clock_label = Label(frm_datetime, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.grid(row=0, column=0, sticky='w')

lbl_date = Label(frm_datetime, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
lbl_date.grid(column = 0, row= 1)

frm_weather = Frame(root)
frm_weather.grid(row=0, column=2, sticky=NW)

lbl_weather_current = Label(frm_weather, text= 'NAO: ' + str(current_temperature), bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_current.grid(row=0,column=0, sticky=NW)

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

update_time()
update_date()

root.mainloop()


