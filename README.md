# Pi Clock

A clock built in Python using Tkinter GUI toolkit to be used with my Raspberry Pi. Along with the time, it displays date and other quick reference information.

It is meant to be used with the official Raspberry Pi 7" touch screen running Rasbian. 


## Screenshots

![SS1](https://raw.githubusercontent.com/kevin-rph-lee/pi-clock/readme/screenshot2.jpg)


![SS1](https://raw.githubusercontent.com/kevin-rph-lee/pi-clock/readme/screenshot1.JPG)

## Features

### Clock

Displays system time, date, day. 

### Weather

Using Accuweather's API, the clock shows current tempurature along with the high/low tempuature and conditions for the next 5 days. This is updated once per hour. 

### Sunrise/Sunset

Checks the Sunrise/Sunset times in Vancouver Canada of the current day. 

### Screen blanking buttons

"Screen on" and "Screen off" buttons use xset command to change how long it will take before the Raspberry Pi screen goes to sleep. 
This uses the xset command to toggle the sleep time between 30 seconds (Screen off) or 1.5 hours (Screen on)

### Sizing to show Discord voice channels

As demonstrated by the screenshot above, the width of the clock is slightly smaller than the width of the Raspberry pi screen. 
This is to allow space for a browser window displaying the voice channels of a Discord server. This gives me the ability to quickly glance at the clock to check if any of my friends have joined a voice channel. 

## ENV File 

Within the env file, add your Accuweather API key. Example setup within .env.example file. 

## Contact

- Email: Kevin.rph.lee@gmail.com
