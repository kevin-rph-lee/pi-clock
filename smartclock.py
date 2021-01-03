from time import strftime
from tkinter import *
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

api_key = "9ec1418c0976ea68fcf8ef36b99f59f4"


window = Tk()
window.title("")
window.configure(bg="green")
window.resizable(False, False)

today = date.today()


clock_label = Label(window, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.grid(column = 0, row= 0, sticky = 'w')

date_label = Label(window, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
date_label.grid(column = 0, row= 1, sticky = 'w')

def update_time():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_time)

# def update_date():
#     current_date = today.strftime("%d-%b-%Y")
#     date_label.configure(text = current_date)
#     date_label.after(80, update_date)

print('Today ' + today.strftime("%d-%b-%Y"))

# print(os.getenv('foo'))


update_time()
# update_date()
window.mainloop()