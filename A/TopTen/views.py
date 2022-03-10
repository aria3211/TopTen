from operator import concat
from django.shortcuts import render
from matplotlib.pyplot import title
from .models import TOP 


def show(request):
   
    allmodels = TOP.objects.all()
    return render(request, 'base.html', {"movies":allmodels})

def show_movie(request,Top_title):
    movie = TOP.objects.get(Title=Top_title)
    return render(request, 'show_base.html', {"info":movie})

def test(request):
    mov = TOP.objects.check(title='The Shawshank Redemption')
    return render(request,'index.html',{"movies":mov})