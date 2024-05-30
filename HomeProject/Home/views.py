from django.shortcuts import render


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
