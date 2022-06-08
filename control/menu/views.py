from django.shortcuts import render, redirect
import serial
import time

#NOTA: Instalar django-tailwind, pip install -r requirements.txt
#NOTA: Usar <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet"> en el base de html.
ser = serial.Serial('COM5', 9600, timeout = 1)
time.sleep(2)

def home(request):
    context = {}
    return render(request, 'menu/home.html', context)

def encender(request):
    if request.method == "GET":
        ser.write(b'P')
        return redirect('home')

def apagar(request):
    if request.method == "GET":
        ser.write(b'N')
        return redirect('home')
    #return render(request, 'menu/apagar.html', context)

def desconectar(request):
    if request.method == "GET":
        ser.close()
        return redirect('home')
