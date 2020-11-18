from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # context = {
    #     "message": "This the message"  #kore wa nani wo shimasuka
    # }
    # return render(request, "index.html", context)
    print('got here from redirect')
    return render(request, 'index.html')

def result(request):
    # if request.method == "GET":
    #     return redirect('/')
    # if request.method == "POST":
        # request.session['']
        
    request.session['name']= request.POST['name']
    request.session['location']= request.POST['location']
    request.session['proglanguage']= request.POST['proglanguage']
    request.session['laptop'] = request.POST['laptop']
    request.session['comment']= request.POST['comment']
    request.session['math'] = request.POST['math']
        
    #     return render(request, "results.html")
    # return render(request, "results.html")
    return redirect('/')