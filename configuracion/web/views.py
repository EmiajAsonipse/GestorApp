from django.shortcuts import render

# Create your views here.
#rederizar es PINTAR
def Home(request):
    return render(request,'index.html')