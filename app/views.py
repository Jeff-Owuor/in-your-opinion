from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import logout,login,authenticate
from .models import Projects,Profile

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'registration/register.html', {"form":form})


def loginPage(request):
    context ={}
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
    
    return render(request,'registration/login.html',context)

def index(request):
    obj = Projects.objects.filter(score=0).order_by('?').first()
    context = {
        'object':obj,
    }
    return render(request,'app/index.html',context)
