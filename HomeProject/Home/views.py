from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Good, Balance


# Create your views here.
def home(request):
    context = {
        'word1': 'kiss',
        'word2': 'me',
        'word3': 'baby',
        'lst': ['apple', 'banana', 'cherry'],
        'info': 'This is a test.'
    }
    return render(request, 'home.html', context)


def example(request):
    return render(request, 'example.html')


def goods_view(request):
    goods_list = Good.objects.filter(quantity__gt=0).all()
    print(goods_list)
    context = {
        "goods": goods_list
    }
    return render(request, 'goods.html', context)


def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            Balance.objects.create(user=register_form.instance)
            redirect('home')
    else:
        register_form = RegisterForm()
    context = {
        'form': register_form
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        login_form = AuthenticationForm()
    context = {
        'form': login_form
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def balance_view(request):
    user = request.user
    balance_to_show = Balance.objects.get(user=user)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        new_balance = Balance.objects.get(user=user)
        new_balance.amount += int(amount)
        new_balance.save()
        return redirect('home')
    return render(request, 'balance.html', {'balance': balance_to_show})
