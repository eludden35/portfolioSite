from django.shortcuts import render, redirect
from .models import *

# *********************************************************
# *********************************************************
# This method will render WELCOME page; welcome page displays register/login links.
def index(request):
    return render(request, 'index.html')

# *********************************************************
# This method will render REGISTER page.

def regTR(request):
    return render(request, 'register.html')

# *********************************************************
# This method will PROCESS FORM info from register page.

def newUser(request):
    isValid = User.objects.regValid(request.POST)
    if len(isValid) > 0:
        for key, value in isValid.items():
            messages.error(request, value)
        return redirect('/')

    newUser = User.objects.create(firstName= request.POST['fname'],lastName= request.POST['lname'],userName= request.POST['uName'],email= request.POST['email'], password= request.POST['pw'])
    request.session['loggedInUser'] = newUser.id
    return redirect('/Homepage')

# *********************************************************
# This method will render LOGIN page.

def logN(request):
    return render(request, 'login.html')




# ==========================================
# ==========================================

# BOOTSTRAP PRACTICE:

def boot(request):
    return render(request, 'bootPrac.html')