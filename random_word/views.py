from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def rand(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    request.session['holder'] = get_random_string(length=14)
    return render(request, 'random.html')

# my reset definition is not resetting the counter as of 11/16 night
def reset(request):
    request.session.flush()
    print('Working!')
    return redirect('/random_word')