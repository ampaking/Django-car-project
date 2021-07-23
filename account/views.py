from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Login')
            return redirect('dashboard')
        else:
            messages.error(request,'User name or password not match')
            return redirect('login')    

    return render(request, 'account/login.html')
def register(request):
    if request.method == 'POST':
        # print('User click register button')
        # messages.error(request, 'Some Error happens Check again')
        # return redirect('register')
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User name already exists, please try something unique')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,first_name=firstname,last_name=lastname)

                        #Django use SHA 252 Hashing tecnic
                    auth.login(request, user)
                    messages.success(request,'Your account is created. You are login')
                    return redirect('dashboard')
                    user.save()
                
                    messages.success(request, 'You are register successfully')
                    return redirect('login')     


        else:
            messages.error(request,'Password does not match')    
    else:    
        return render(request, 'account/register.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out')
        return redirect('home')
    return redirect('home')
def dashboard(request):
    return render(request, 'account/dashboard.html')