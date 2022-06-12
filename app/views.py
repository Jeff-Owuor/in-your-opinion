from django.shortcuts import render,redirect
from .forms import RegisterForm,UploadProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from .models import Projects,Profile
from django.http import JsonResponse

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

def logout_user(request):
    logout(request)
    return redirect('login')

def index(request):
    obj = Projects.objects.filter(score=0).order_by('?').first()
    context = {
        'object':obj,
    }
    return render(request,'app/index.html',context)


def rate_image(request):
    if request.method == 'POST':
        element_id = request.post.get('element_id')
        val = request.post.get('val')
        obj = Projects.objects.get(id = element_id)
        obj.score = val
        obj.save()
        
        return JsonResponse({"success":'true','score':val}, safe=False)
    
    return JsonResponse({'success':'false'})

@login_required(login_url='login/')
def projectUpload(request):
    current_user  = request.user
    profile_instance = Profile.objects.get(user=current_user)
    if request.method =='POST':
        form = UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile_instance
            project.save()
        return redirect('home')
    else:
        form  = UploadProjectForm()
        context  = {
            "form":form
            }
    return render(request, 'app/post.html', context)
