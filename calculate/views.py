from django.shortcuts import render
from solutions.solution_one import perform_compute_1
from solutions.solution_three import perform_compute_2
import json
from django.http import JsonResponse


def index(request):
    return render(request, "calculate/calculate.html")


def calculate(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        x = int(data.get('x', None))
        n= int(data.get('n', None))
    
        answer = perform_compute_1(x,n)

        return JsonResponse({"answer": answer}, status=200)
    
