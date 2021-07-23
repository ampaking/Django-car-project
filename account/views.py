from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'account/login.html')
def register(request):
    if request.method == 'POST':
        print('User click register button')
        return redirect('regester')
    else:    
        return render(request, 'account/register.html')
def logout(request):
    return redirect('home')
def dashboard(request):
    return render(request, 'account/dashboard.html')