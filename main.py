from tkinter import *
import requests
import json


root=Tk();
root.title("Weather App");


def zipLookup():
    try:
        api_request = requests.get(f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip.get()}&distance=25&API_KEY=16D0C1E0-6E73-41A7-A9F2-EA76BDDF7A62');
        api = json.loads(api_request.content);
        city = api[0]['ReportingArea'];
        aqi = api[0]['AQI'];
        category = api[0]['Category']['Name'];
    except Exception:
        api = 'Error';    
    
    
    weather_color = 'white';
    
    
    if api!='Error':
        if category == 'Good':
            weather_color = '#0c0';
        elif category == 'Moderate':
            weather_color = '#FFFF00';
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff9900';
        elif category == 'Unhealthy':
            weather_color = '#FF0000';
        elif category == 'Very Unhealthy':
            weather_color = '#990066';              
        elif category == 'Hazardous':
            weather_color = '#660000';  
        
        root.config(bg=weather_color);                        
        
        weatherLabel = Label(root, text=f'{city} Air Quality:{aqi} {category}', bg=weather_color, font=('Sans-Serif',10));
        weatherLabel.grid(row=1, column=0);
    else:    
        weatherLabel = Label(root, text='Internet connection problem or area not found', bg=weather_color);
        weatherLabel.grid(row=1, column=0);
    

zip = Entry(root);
zip.grid(row=0, column=0, stick=W+E+N+S);


submitZipButton = Button(root, text='Lookup Zip', command=zipLookup);
submitZipButton.grid(row=0, column=1, stick=W+E+N+S);


root.mainloop();