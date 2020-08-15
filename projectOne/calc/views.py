from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#Function accepts request from client
#So whenever a client requests the home page, we return hello world
#We use http to send data in a response 
# format since we are getting data in a request format

def home(request):
    return render(request, 'home.html', {'name':'Erick Nyoro'})

###<!--Once submit is clicked, request goes to add, now go and sort that
                ###out in urls.py (calc)-->

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1+val2
    return render(request, 'result.html',{'Result':res})