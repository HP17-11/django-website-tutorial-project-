from django.shortcuts import render, redirect
from .models import Profile, Skill
from projects.models import Project
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, SkillForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.


def loginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            print(user)

        except:
            messages.error(request, "username doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "you are logged in!!!")
            return redirect('profiles')

        else:
            messages.error(
                request, 'Either Username or Password is incorrect!')

    return render(request, 'users/loginregister.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'User has logged out!!!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User is created!!!')
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'error has occured!!!')

    context = {'page': page, 'form': form}
    return render(request, 'users/loginregister.html', context)


@login_required(login_url='login')
def userAccount(request):

    ruser = request.user
    useraccount = Profile.objects.get(user=ruser)
    context = {'user': useraccount}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def addskill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = profile
            skill.save()
            messages.success(request, 'Skill was created!!!')
            return redirect('account')

    context = {'form': form, }
    return render(request, 'users/skillform.html', context)

@login_required(login_url='login')
def updateskill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated!!!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skillform.html', context)

@login_required(login_url='login')
def deleteskill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    
    
    if request.method == 'POST':
        skill.delete()
        messages.error(request, 'Skill was deleted!!!')
        return redirect('account')
    
    context = {'object':skill}
    return render(request,'projects/delete_template.html', context)

@login_required(login_url='login')
def editaccount(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        
        if form.is_valid():
            form.save() 
            return redirect('account')

    context = {'form': form }
    return render(request, 'users/useraccount-profile.html', context)



def profiles(request):

    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userprofile(request, p):
    uprofile = Profile.objects.get(id=p)
    otherskills = uprofile.skill_set.filter(description='')
    topskills = uprofile.skill_set.exclude(description__exact='')
    context = {'userprofile': uprofile,
               'otherskills': otherskills, 'skills': topskills}
    return render(request, 'users/user-profile.html', context)
