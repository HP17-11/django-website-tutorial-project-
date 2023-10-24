from re import A
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag,Review
from .forms import Projectform
from django.contrib.auth.decorators import login_required 
from users.models import Profile


@login_required(login_url='login')
def createproject(request):
    
    form = Projectform()
    profile = request.user.profile 

    if request.method=="POST":
        #print(request.POST)
        form = Projectform(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def updateproject(request, n):
    profile = request.user.profile 
    project = profile.project_set.get(id=n)
    #project = Project.objects.get(id=n)
    form = Projectform(instance = project)
    
    if request.method=="POST":
       
        form = Projectform(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('account')
    

    context = {'form': form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteproject(request, n) :
    profile = request.user.profile 
    project = profile.project_set.get(id=n)
    context = {'object': project}

    if request.method=='POST' :
        project.delete()
        return redirect('projects')

    return render(request, 'projects/delete_template.html',context)


def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'project1':projects})


def project(request, n):
    projectObj = Project.objects.get(id=n)
    tags1 = projectObj.tags.all()
    return render(request,'projects/singleproject.html', {'project2': projectObj , 'tag':tags1})

