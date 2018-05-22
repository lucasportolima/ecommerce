from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    texts = ["lorad jasd jkasdkajbskasdf ds", "l sfkjdsbfsfskf  sjdfsça sdhf sufeueuu", "huauhauhauhuahhuehuehueheuheuheu"]
    context = {
        'title': 'django e-commerce',
        'texts': texts
    }

    return render(request, 'index.html', context)
