from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "message": "This the message"  #kore wa nani wo shimasuka
    }
    return render(request, "index.html", context)

def result(request):
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        # request.session['']
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'proglanguage': request.POST['proglanguage'],
            'laptop' : request.POST['laptop'],
            'comment': request.POST['comment'],
            'math' : request.POST['math'],
        }
        return render(request, "results.html", context)
    return render(request, "result.html")