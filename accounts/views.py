from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
from accounts.forms import UserRegistrationForm
from accounts.serializers import AccountsSerializer
from rest_framework import viewsets
from django.views.decorators.cache import cache_page

User = get_user_model()

# Create your views here.
class AccountsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountsSerializer

# @login_required(login_url='Login')
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    
    # form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return render(request, 'home.html')
            # return redirect('accounts/login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def sign_in(request):

    form = LoginForm()

    if request.method == "POST":
        usrname = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username=usrname, password=pwd)
        print('this is user ', type(user))
        if user is not None:
            login(request, user)
           
            return render(request, 'home.html', {'user': user})
            # return redirect('/accounts')

    context={'form': form}

    return render(request, 'login.html', context)

def log_out(request):

    logout(request)
    print('logged out!')

    return redirect('/accounts')