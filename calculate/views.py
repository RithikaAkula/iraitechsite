from django.shortcuts import render
from solutions.solution_one import perform_compute_1
from solutions.solution_three import perform_compute_2

# Create your views here.

def index(request):
    return render(request, "calculate/calculate.html")


def calculate(request):

    x = request.POST['x']
    n = request.POST['n']

    if x.isdigit() and n.isdigit():
        x=int(x)
        n=int(n)

        result = perform_compute_1(x,n)

        return render(request,"calculate/result.html",{"result": result})
    else:
        res="Only integers allowed"
        return render(request, "calculate/result.html", {"result": res})


def calculate_two(request):

    x = request.POST['x']
    y = request.POST['y']
    a = request.POST['a']
    b = request.POST['b']


    if x.isdigit() and y.isdigit() and a.isdigit() and b.isdigit():
        x=int(x)
        y=int(y)
        a=int(a)
        b=int(b)
        
        result = perform_compute_2(x,y,a,b)

        return render(request,"calculate/result.html",{"result": result})
    else:
        res="Only integers allowed"
        return render(request, "calculate/result.html", {"result": res})
