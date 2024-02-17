from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
from todoApp.forms import TODOForm
from todoApp.models import TODO
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import ASCIIUsernameValidator, ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'home.html' , context={'form' : form , 'todos' : todos})

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not all([uname, email, pass1, pass2]):
            messages.error(request, "Please fill in all fields.")
        else:
            # Validate email
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, "Please enter a valid email address.")
                return render(request, 'signup.html')

            # Validate password strength
            if not (any(char.isdigit() for char in pass1) and any(char.isalpha() for char in pass1) and any(not char.isalnum() for char in pass1)):
                messages.error(request, "Password must contain at least one letter, one number, and one special character.")
                return render(request, 'signup.html')

            # Check if passwords match
            if pass1 != pass2:
                messages.error(request, "Your password and confirm password are not the same.")
                return render(request, 'signup.html')

            # Check if username already exists
            if User.objects.filter(username=uname).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
                return render(request, 'signup.html')

             # Hash the password
            hashed_pass = make_password(pass1)

            # Create user
            my_user = User.objects.create_user(uname, email,pass1 )
            my_user.save()

            messages.success(request, "Your account has been created successfully.")
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Use 'password', not 'hashed_pass'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You're successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!!!")

    return render(request, 'login.html')
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            messages.success(request, "Task Added Successfully")
            #print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})


def delete_todo(request , id ):
    #print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

def edit_todo(request, id):
    if request.method == 'POST':
        todo = TODO.objects.get(pk=id)
        form = TODOForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        todo = TODO.objects.get(pk=id)
        form = TODOForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})

def onboarding(request):
    return render(request, 'onboarding.html')  # Assuming you have an onboarding HTML template


def signout(request):
    logout(request)
    return redirect('login')