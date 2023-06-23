from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    print("POST!")
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    return redirect('/show')

def show(request):
    return render(request, 'show.html')