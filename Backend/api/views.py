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

# def test(request):
#     req = requests.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
#     raw = req.text
#     html = BeautifulSoup(raw, 'html.parser')
#     infos = html.select('table.highlight.tab-size.js-file-line-container')
#     infos = infos[0]
#     context = {
#         'infos': infos,
#     }
#     return render(request, 'api/test.html', context)
