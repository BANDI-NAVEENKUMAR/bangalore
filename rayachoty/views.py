from django.shortcuts import render

# Create your views here.
def traveling(request):
    return render(request,'ticket.html')