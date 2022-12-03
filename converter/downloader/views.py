
from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse

from pytube import *

# Create your views here.
def youtube(request):

    #valida si el metodo http es post a la hora de ingresar el link
    if request.method == "POST":
        link = request.POST['link']
        video = YouTube(link)

        #configurammos la calidad de video
        quality = request.POST['quality']
        
        if quality == "high":
        
            stream = video.streams.get_highest_resolution()
            stream.download()
        
        else:
            stream = video.streams.get_lowest_resolution()
            stream.download()
    return render(request, 'form.html')
"""
         stream = video.streams.get_lowest_resolution()

        #descargamos el video
        stream.download() 
"""
