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


response_current = requests.get(url_current) 
response_forecast = requests.get(url_forecast) 

current_json = response_current.json()
forecast_json = response_forecast.json() 


current_temperature = current_json[0]['Temperature']['Metric']['Value']
# print(current_temperature)

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

clock_label = Label(root, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.grid(row=0, column=0, sticky='w')

lbl_date = Label(root, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
lbl_date.grid(column = 0, row= 1)

frm_weather = Frame(root)
frm_weather.grid(row=0, column=2, sticky=NW)

lbl_weather_today = Label(frm_weather, text= 'Today: ' + str(current_temperature), bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather_today.grid(row=0,column=0, sticky=NW)

# lbl_weather_2nd_day = Label(frm_weather, text= 'Today: ' + str(current_tempurature), bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
# lbl_weather_2nd_day.grid(row=1,column=0, sticky=NW)


weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# print(weather_json)

# g = Button(frm_weather, text="quit")
# # g.grid(row=1,column=0, sticky=NW)
# print(weekDays[today_date.weekday()])
# print(findDay(date.today()))

update_time()
update_date()

root.mainloop()


