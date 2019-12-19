from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Algorithm
from .serializers import AlgorithmSerializer

import ast
# Create your views here.

import requests



@api_view(['GET'])  
def problem_list(request):
    problems = Algorithm.objects.all()
    serializer = AlgorithmSerializer(problems, many=True)
    return Response(serializer.data)

def api_doc(request):
    return redirect('api/v1/swagger/')

@api_view(['GET'])
def get_source(request, prob_pk):
    problem = get_object_or_404(Algorithm, pk=prob_pk)
    code_url = problem.code_url
    req = requests.get(code_url)
    raw = req.text
    start = 0
    end = 0
    for i in range(len(raw)):
        if raw[i] == '<' and raw[i+1] == 't' and raw[i+2] == 'a' and raw[i+3] == 'b' and raw[i+4] == 'l' and raw[i+5] == 'e':
            start = i
        if raw[i] == '<' and raw[i+1] == '/' and raw[i+2] == 't' and raw[i+3] == 'a' and raw[i+4] == 'b' and raw[i+5] == 'l':
            end = i + 8
            break
    table_ele = raw[start:end]
    return Response(table_ele)