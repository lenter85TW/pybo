from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Question
import json



def index(request):
    # return HttpResponse("안녕하세요 pybo3에 오신것을 환영합니다.")
    question_list = Question.objects.order_by('-create_date')
    context = {'questionlist': question_list}
    return render(request, 'pybo/question_list.html', context)

def my(request):
    print('fail?')
    if request.method == 'POST':
        json_data = json.loads(request.body)

        print('json data request arrived : ', json_data)

        response_data = {'message':'Success'}
        return JsonResponse(response_data)