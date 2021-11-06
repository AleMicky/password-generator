from django.shortcuts import render
import random

def home(request):
    return render(request,'generator/home.html')

def about(request):
   return render(request,'generator/about.html')

def generatedPassword(request):

    generated_password = ''
 

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){}[]'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 10))

    for x in range(length):
        generated_password += random.choice(characters)


    return render(request, 'generator/password.html', {'password': generated_password})
