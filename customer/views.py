from django.shortcuts import render
from home.models import *
from django.http import HttpResponse
from datetime import *
# Create your views here.


def customer(request):
    template_name = 'customer/customer_index.html'

    customers = Customer.objects.all()
    context = {'customers': customers}

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


