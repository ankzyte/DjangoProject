from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'{username} successfully registered! Login to continue')
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    return render(request,"user/register.html",{'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request,f'successfully updated profile!')
            return redirect('user-profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)
    context={
        'uForm':uForm,
        'pForm':pForm
    }
    return render(request,"user/profile.html",context)