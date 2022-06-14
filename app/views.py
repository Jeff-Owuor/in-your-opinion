from django.shortcuts import render,redirect
from .forms import RegisterForm,UploadProjectForm,RatingsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from .models import Projects,Profile,Review
from django.http import JsonResponse
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy

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
    projects = Projects.objects.all()
    obj = Projects.objects.filter(score=0)
    context = {
        'object':obj,
        'projects':projects
    }
    return render(request,'app/index.html',context)

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

@login_required(login_url='login/')
def profile(request, id):
    profile = Profile.objects.get(user=id)
    userid = request.user.id
    user_posts = profile.projects_set.all()
    
    context={
        "profile":profile,
        "userid":userid,
        'user_posts': user_posts,
    }
    return render(request, 'app/user_profile.html',context)


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'app/edit.html'
    fields = ['bio','profile_photo','github','instagram','linkedin']
    success_url = reverse_lazy('home')
    

@login_required(login_url='login/')
def rate_project(request, id):
    project = Projects.objects.get(id=id)
    user = request.user
    
    if request.method =='POST':
        form = RatingsForm(request.POST)
        
        if form.is_valid():
            rate_design = form.save(commit=False)
            rate_design.user = user
            rate_design.project = project
            rate_design.save()
            return redirect('home')
        
    else:
        form = RatingsForm()
        
    return render(request, 'app/rate_project.html',{"project":project,"ratingform":form})

def single_project(request,id):
    project = Projects.objects.get(id=id)
    reviews = Review.objects.filter(project=id)
    
    context = {
        "project":project,
        "reviews":reviews
    }
    return render(request,'app/single_project.html',context)


def search_project(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        project = Projects.objects.filter(project_title__icontains=searched).all()
        params = {
            'searched':searched,
            'projects':project
        }
        return render(request, 'app/results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'app/results.html', {'message': message})