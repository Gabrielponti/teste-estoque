from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('stock_list_view')
    else:
        user_form = UserCreationForm()
    return render(
        request=request,
        template_name='register.html',
        context={'user_form': user_form}

    )


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stock_list_view')
        else:
            login_form = AuthenticationForm()

    login_form = AuthenticationForm()

    return render(
        request=request,
        template_name='login.html',
        context={'login_form': login_form}
    )


def logout_view(request):
    logout(request=request)
    return redirect('login')
