from time import strftime
from tkinter import *
from datetime import date
from dotenv import load_dotenv
import os
import requests, json 



load_dotenv()

api_key = os.getenv('API')
# city_name = input("Enter city name : ") 

complete_url = 'https://api.openweathermap.org/data/2.5/onecall?units=metric&lat=49.17&lon=-123.14&exclude=minutely&appid=' +  api_key

response = requests.get(complete_url) 

weather_json = response.json() 

root = Tk()
root.geometry("480x320")
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=0)

today_date = date.today()
current_tempurature = weather_json['current']['temp']


def update_time():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_time)

def update_date():
    current_date = today_date.strftime("%d-%b-%Y")
    lbl_date.configure(text = current_date)
    lbl_date.after(80, update_date)

clock_label = Label(root, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.grid(row=0, column=0, sticky='w')

lbl_date = Label(root, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
lbl_date.grid(column = 0, row= 1)

frm_weather = Frame(root)
frm_weather.grid(row=0, column=2, sticky=NW)

lbl_weather = Label(frm_weather, text= 'Today: ' + current_tempurature, bg="blue", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_weather.grid(row=0,column=0, sticky=NW)

g = Button(frm_weather, text="quit")
g.grid(row=1,column=0, sticky=NW)

update_time()
update_date()

root.mainloop()


