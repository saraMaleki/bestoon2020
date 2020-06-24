from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from poll.models import User, Token, Expense, Income
from datetime import datetime

# Create your views here.

@csrf_exempt
def Submit_Expense(request):
    print(request.POST)

    this_token = request.POST['token']
    this_user = User.objects.filter(token__text=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']

    Expense.objects.create(user=this_user, amount=request.POST['amount'], date=date, text=request.POST['text'])

    return JsonResponse({
        'status': 'OK',
    }, encoder=JSONEncoder)


@csrf_exempt
def Submit_Income(request):
    print(request.POST)

    this_token = request.POST['token']
    this_user = User.objects.filter(token__text=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']

    Income.objects.create(user=this_user, amount=request.POST['amount'], date=date, text=request.POST['text'])

    return JsonResponse({
        'status': 'OK',
    }, encoder=JSONEncoder)

