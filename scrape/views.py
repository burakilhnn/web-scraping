from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .scrape import *

urls = []

def home(request):
    return render(request, 'scrape/home.html',{'urls':urls})

def compare(request):
    first_array = scrape(urls[-2])
    second_array = scrape(urls[-1])
    first_unq = make_unique(first_array)
    second_unq = make_unique(second_array)
    first_unq = throw_numbers(first_unq)
    second_unq = throw_numbers(second_unq)
    first_keywords = bubble_sort(first_unq,first_array)
    second_keywords = bubble_sort(second_unq,second_array)
    comp = compare_url(first_keywords, second_keywords)
    first_freqs = list_of_frequencies(first_unq, first_array)
    second_freqs = list_of_frequencies(second_unq,second_array)
    context = {
        'fdatas':first_keywords,
        'sdatas':second_keywords,
        'comp':comp,
        'ffreqs':first_freqs,
        'sfreqs':second_freqs,
        'funq':first_unq,
        'sunq':second_unq,
    }
    return render(request, 'scrape/compare.html',context)
    
@require_POST
def send(request):
    if request.method == 'POST':
        urls.append(request.POST['firstUrl'])
        urls.append(request.POST['secondUrl'])
    return redirect('scrape:compare')