from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):

    basket = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        basket.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        basket.extend(list('1234567890'))

    if request.GET.get('special character'):
        basket.extend(list('!@#$%&*_'))

    length = int(request.GET.get('length',12))

    
    finalpassword = ''

    for x in range(length):
        finalpassword += random.choice(basket);

    return render(request,'generator/password.html',{'password' : finalpassword })


def about(request):
    return render(request,'generator/about.html')