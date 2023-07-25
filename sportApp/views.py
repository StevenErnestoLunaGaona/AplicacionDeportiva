from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def futbol(request):
    return render(request, 'futbol.html')

def basquetbol(request):
    return render(request, 'basquetbol.html')

def ajedrez(request):
    return render(request, 'ajedrez.html')

def pingpong(request):
    return render(request, 'pingpong.html')

def noticia(request):
    return render(request, 'noticia.html')

def calendario(request):
    return render(request, 'calendario.html')

def about(request):
    return render(request, 'about.html')
