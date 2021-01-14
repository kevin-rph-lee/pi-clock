from time import strftime
from tkinter import *
from datetime import *
from dotenv import load_dotenv
import os
import requests, json 
import calendar 

load_dotenv()

api_key = os.getenv('API')

url_current = 'http://dataservice.accuweather.com/currentconditions/v1/47173?apikey=' + api_key
url_forecast = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/47173?apikey=' + api_key + '&metric=true'

weekDays = ("M ","Tu","W ","Th","F ","Sa","Su")

response_current = requests.get(url_current) 
response_forecast = requests.get(url_forecast) 

current_json = response_current.json()
forecast_json = response_forecast.json() 


current_temperature = current_json[0]['Temperature']['Metric']['Value']

# print(forecast_json['DailyForecasts'])

# date_day1 = forecast_json['DailyForecasts'][0]['Date']
date_day1 = weekDays[date.today().weekday()]
temp_low_day1 = str(forecast_json['DailyForecasts'][0]['Temperature']['Minimum']['Value'])
temp_high_day1 = str(forecast_json['DailyForecasts'][0]['Temperature']['Maximum']['Value'])

date_day2 = weekDays[(date.today()+ timedelta(1)).weekday()]
temp_low_day2 = str(forecast_json['DailyForecasts'][1]['Temperature']['Minimum']['Value'])
temp_high_day2 = str(forecast_json['DailyForecasts'][1]['Temperature']['Maximum']['Value'])

date_day3 = weekDays[(date.today()+ timedelta(2)).weekday()]
temp_low_day3 = str(forecast_json['DailyForecasts'][2]['Temperature']['Minimum']['Value'])
temp_high_day3 = str(forecast_json['DailyForecasts'][2]['Temperature']['Maximum']['Value'])

date_day4 = weekDays[(date.today()+ timedelta(3)).weekday()]
temp_low_day4 = str(forecast_json['DailyForecasts'][3]['Temperature']['Minimum']['Value'])
temp_high_day4 = str(forecast_json['DailyForecasts'][3]['Temperature']['Maximum']['Value'])

date_day5 = weekDays[(date.today()+ timedelta(4)).weekday()]
temp_low_day5 = str(forecast_json['DailyForecasts'][4]['Temperature']['Minimum']['Value'])
temp_high_day5 = str(forecast_json['DailyForecasts'][4]['Temperature']['Maximum']['Value'])



root = Tk()
root.geometry("480x320")
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=0)

today_date = date.today()



def update_time():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_time)

def update_date():
    current_date = today_date.strftime("%d-%b-%Y")
    lbl_date.configure(text = current_date)
    lbl_date.after(80, update_date)


def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

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

lbl_weather_today = Label(frm_weather, text= f'Date: {date_day1} High: {temp_high_day1} Low: {temp_low_day1}', bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_today.grid(row=1,column=0, sticky=NW)

lbl_weather_today = Label(frm_weather, text= f'Date: {date_day2} High: {temp_high_day2} Low: {temp_low_day2}', bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_today.grid(row=2,column=0, sticky=NW)

lbl_weather_today = Label(frm_weather, text= f'Date: {date_day3} High: {temp_high_day3} Low: {temp_low_day3}', bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_today.grid(row=3,column=0, sticky=NW)

lbl_weather_today = Label(frm_weather, text= f'Date: {date_day4} High: {temp_high_day4} Low: {temp_low_day4}', bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_today.grid(row=4,column=0, sticky=NW)

lbl_weather_today = Label(frm_weather, text= f'Date: {date_day5} High: {temp_high_day5} Low: {temp_low_day5}', bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_today.grid(row=5,column=0, sticky=NW)


update_time()
update_date()

root.mainloop()


