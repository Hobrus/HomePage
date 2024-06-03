from django.shortcuts import render

from .models import Good


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
