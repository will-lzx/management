from django.shortcuts import render
from home.models import *
from django.http import HttpResponse
from datetime import *
# Create your views here.
from home.templatetags.own_tag import get_lendcount


def customer(request):
    template_name = 'customer/customer_index.html'

    customers = Customer.objects.all()

    context = {
        'menu_selected': 'user_management',
        'customers': customers
    }

    response = render(request, template_name, context)
    return response


def search(request):
    weixin_number = request.POST.get('weixin_number')
    mobile_number = request.POST.get('mobile_number')
    deposit_status = request.POST.get('deposit_status')

    if weixin_number:
        if mobile_number:
            if deposit_status:
                customers = Customer.objects.filter(weixin_number__contains=weixin_number, mobile_number__contains=mobile_number, deposit=deposit_status)
            else:
                customers = Customer.objects.filter(weixin_number__contains=weixin_number,
                                                    mobile_number__contains=mobile_number)
        else:
            if deposit_status:
                customers = Customer.objects.filter(weixin_number__contains=weixin_number, deposit=deposit_status)
            else:
                customers = Customer.objects.filter(weixin_number__contains=weixin_number)
    else:
        if mobile_number:
            if deposit_status:
                customers = Customer.objects.filter(mobile_number__contains=mobile_number, deposit=deposit_status)
            else:
                customers = Customer.objects.filter(mobile_number__contains=mobile_number)
        else:
            if deposit_status:
                customers = Customer.objects.filter(deposit=deposit_status)
            else:
                customers = ''

    html = get_customer(customers)
    return HttpResponse('Success&' + html)


def get_customer(customers):
    html = '<table><tr><td>微信号</td>' \
           '<td>手机号</td>' \
           '<td>支付宝帐号</td>' \
           '<td>蚂蚁信用分</td>' \
           '<td>押金</td>' \
           '<td>注册时间</td>' \
           '<td>租用次数</td>' \
           '<td>操作</td></tr>'

    if not customers:
        html += '<tr><td colspan="6">No customers still</td></tr>'
    else:
        for customer in customers:
            html += '<tr><td>' + str(customer.weixin_number) \
                    + '</td><td>' + str(customer.mobile_number) + '</td><td>' \
                    + str(customer.alipay) + '</td><td>' \
                    + str(customer.credit_score) + '</td><td>' \
                    + str(customer.deposit) + '</td><td>' \
                    + str(customer.create_time.strftime('%Y-%m-%d %H:%M:%S')) + '</td><td>' \
                    + str(get_lendcount(customer.weixin_number)) + '</td><td><a href="/customer/lendhistory/' \
                    + str(customer.mobile_number) +'" >租借详情</a></td></tr>'

    html += '</table>'
    return html


def lendhistory(request, mobile_number):
    lendhistories = LendHistory.objects.filter(mobile_number=mobile_number).order_by('-start_time')
    template_name = 'customer/lendhistory_by_customer.html'

    context = {'lendhistories': lendhistories}

    response = render(request, template_name, context)
    return response


def lendmanagement(request):
    lendhistories = LendHistory.objects.all().order_by('-start_time')
    template_name = 'customer/lendmanagement.html'

    context = {
        'menu_selected': 'lend_management',
        'lendhistories': lendhistories
    }

    response = render(request, template_name, context)
    return response


def rule(request):
    template_name = 'customer/rule/rule.html'
    rules = Rule.objects.all().order_by('-modify_time')
    context = {'rules': rules}
    response = render(request, template_name, context)
    return response


def rule_add(request):
    time_long = request.POST.get('time_long')
    unit_price = request.POST.get('unit_price')
    is_valid = request.POST.get('is_valid')
    operator = request.POST.get('operator')
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    modify_time = create_time
    try:
        rule = Rule(start_time_long=time_long, unit_price=unit_price, is_valid=is_valid, create_time=create_time, modify_time=modify_time, operator=operator)
        rule.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_rules()
    return HttpResponse('Success&' + html)


def rule_update(request, rule_id):
    rule = Rule.objects.filter(id=rule_id).first()
    template_name = 'customer/rule/rule_update.html'
    context = {'rule': rule}
    response = render(request, template_name, context)
    return response


def rule_update_submit(request):
    time_long = request.POST.get('time_long')
    unit_price = request.POST.get('unit_price')
    is_valid = request.POST.get('is_valid')
    operator = request.POST.get('operator')
    modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    rule_id = request.POST.get('rule_id')
    rule = Rule.objects.filter(id=rule_id).first()
    try:
        rule.start_time_long = time_long
        rule.unit_price = unit_price
        rule.is_valid = is_valid
        rule.modify_time = modify_time
        rule.operator = operator
        rule.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    return HttpResponse('Success&')


def rule_delete(request):
    id = request.POST.get('rule_id')
    unit_price = request.POST.get('unit_price')
    is_valid = request.POST.get('is_valid')
    operator = request.POST.get('operator')
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    modify_time = create_time
    rule = Rule.objects.filter(id=id)
    try:
        rule.delete()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_rules()
    return HttpResponse('Success&' + html)


# help methods
def get_rules():
    html = '<table><tr>' \
           '<td rowspan="2">开始时间长度</td>' \
           '<td rowspan="2">单价</td>' \
           '<td rowspan="2">是否生效</td>' \
           '<td rowspan="2">创建时间</td>' \
           '<td rowspan="2">修改时间</td>' \
           '<td rowspan="2">操作人</td>' \
           '<td colspan="2">操作</td></tr><tr>' \
           '<td>更新</td>' \
           '<td>删除</td></tr>'
    rules = Rule.objects.all().order_by('-modify_time')
    if rules:
        for rule in rules:
            if rule.is_valid == 1:
                is_valid = '是'
            else:
                is_valid = '否'
            html += '<tr><td>' + str(rule.start_time_long) + '</td><td>' \
                    + str(rule.unit_price) + '</td><td>' \
                    + is_valid + '</td><td>' \
                    + str(rule.create_time.strftime('%Y-%m-%d %H:%M:%S')) + '</td><td>' \
                    + str(rule.modify_time.strftime('%Y-%m-%d %H:%M:%S')) + '</td><td>' \
                    + rule.operator + '</td><td><a href="/customer/rule/rule_update/' + str(rule.id) \
                    + '">更新</a></td><td><a href="#" onclick="delete_rule(\'' \
                    + str(rule.id) +'\')">删除</a></td></tr>'

    html += '</table>'
    return html


