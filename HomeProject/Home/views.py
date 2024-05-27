from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'word1': 'kiss',
        'word2': 'me',
        'word3': 'baby',
    }
    return render(request, 'home.html', context)
