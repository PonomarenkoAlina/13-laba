import tkinter as tk
import requests

def get_weather(city):
    weather_key = 'c9ce3d25a6e5fb7756d166edc02ff12d'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

def format_response(weather):
    try:
        city_name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        final_str = 'Город: %s nСостояние: %s nТемпература (°C): %s' % (city_name, description, temperature)
    except:
        final_str = 'Произошла ошибка при получении информации'

    return final_str

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

frame = tk.Frame(root, bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Получить погоду", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#42c2f4', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
