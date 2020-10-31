from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'accounts/home.html')


# class LoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'accounts/login.html'
#     success_url=reverse_lazy('home')

# class RegisterView(generic.CreateView):
#     form_class = RegisterForm
#     template_name = 'accounts/register.html'
#     success_url = reverse_lazy('login')

def signup(request):
    if request.method=="POST":
        forms=RegisterForm(request.POST)
        if forms.is_valid():
            password1=forms.cleaned_data['password1']
            password2= forms.cleaned_data['password2']
            username=forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            contact=forms.cleaned_data['contact']
            if password1==password2:
                user=CustomUser.objects.create_user(username=username,email=email,password=password1,contact=contact)
                user.save()
                return redirect('login')
            else:
                print("check your credential")
                return redirect('signup')
        else:
            forms = RegisterForm()
            return render(request,'accounts/register.html',{"forms":forms})
    else:
        forms = RegisterForm()
        return render(request, 'accounts/register.html', {"forms": forms})
    return render(request, 'accounts/register.html', {"forms": forms})

def Login(request):
    if request.method=="POST":
        forms=LoginForm(request.POST)
        print(forms.data)
        if forms.is_valid():
            password=forms.cleaned_data['password']
            username=forms.cleaned_data['username']
            print(username)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                print('user is none')
                return redirect('login')
        else:
            print('form is in valid')
            return render(request, 'accounts/login.html', {"forms": forms})
    else:
        print('form is in valid2')
        forms=LoginForm()
        return render(request, 'accounts/login.html', {"forms": forms})
    return render(request, 'accounts/login.html', {"forms": forms})

def Logout(request):
    logout(request)
    return redirect('home')