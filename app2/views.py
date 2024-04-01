from django.shortcuts import render

# Create your views here.
def app2_firstapp(request):
    return render(request,'html2.html')

def app2_secondapp(request):
    return render(request,'html2.html')