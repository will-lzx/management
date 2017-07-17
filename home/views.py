from datetime import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from management.settings import *
from home.models import *

# Create your views here.


def home(request):
    template_name = 'home/home.html'

    today = datetime.now().replace(hour=0, second=0, minute=0)
    new_customer_count = len(Customer.objects.filter(create_time__gte=today))

    lend_count_today = len(LendHistory.objects.filter(start_time__gte=today))

    today_lends = LendHistory.objects.filter(start_time__gte=today).all()
    today_money = 0
    for lend in today_lends:
        today_money += lend.money

    today_deposits = Customer.objects.filter(create_time__gte=today).all()

    today_deposit = 0
    for deposit in today_deposits:
        today_deposit += deposit.deposit

    total_customer_count = len(Customer.objects.all().distinct().values('mobile_number'))

    total_lend_count = len(LendHistory.objects.all())

    total_deposits = Customer.objects.all()

    total_deposit = 0
    for deposit in total_deposits:
        total_deposit += deposit.deposit

    spot_counts = len(Spot.objects.all())

    pole_counts = len(Pole.objects.all())
    context ={
            'menu_selected': 'home',
            'new_customer_count': str(new_customer_count),
            'lend_count_today': str(lend_count_today),
            'today_money': today_money,
            'today_deposit': today_deposit,
            'total_customer_count': total_customer_count,
            'total_lend_count': total_lend_count,
            'total_deposit': total_deposit,
            'spot_counts': spot_counts,
            'pole_counts': pole_counts
        }
    response = render(request, template_name, context)
    return response


def home_login(request):
    template_name = 'login/login.html'
    response = render(request, template_name)
    return response


def home_logon(request):
    mobile_number = request.POST.get('mobile_number')
    verify_code = request.POST.get('verify_code')
    if not check_verify_code(verify_code):
        return HttpResponse('Fail&verify_code wrong')

    check_user = User.objects.filter(username=str(mobile_number))

    if not check_user:
        user = User.objects.create_user(str(mobile_number), tmp_mail, tmp_pwd)
        user.save()
    user = authenticate(username=str(mobile_number), password=tmp_pwd)
    login(request, user)
    return HttpResponse('Success&Login successfully')


def home_logout(request):
    # mobile_number = request.POST.get('mobile_number')
    # user = authenticate(username=str(mobile_number), password=tmp_pwd)
    logout(request)
    template_name = 'login/login.html'
    response = render(request, template_name)
    return response


def agreement(request):
    template_name = 'login/agreement.html'
    response = render(request, template_name)
    return response


def check_verify_code(verify_code):
    return True
