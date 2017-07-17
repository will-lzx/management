from django.shortcuts import render
from home.models import *
from django.http import HttpResponse
from datetime import *
# Create your views here.


def hardware(request):
    template_name = 'hardware/hardware_index.html'
    response = render(request, template_name)
    return response


def cabinet(request):
    cabinets = Cabinet.objects.all().order_by('number')
    spots = Spot.objects.all()
    context = {
        'menu_selected': 'cabinet_management',
        'cabinets': cabinets,
        'spots': spots
    }
    template_name = 'hardware/cabinet/cabinet.html'
    response = render(request, template_name, context)
    return response


def cabinet_add(request):
    number = request.POST.get('number')
    two_dimension = request.POST.get('two_dimension')
    spot_id = request.POST.get('spot_id')
    capacity = request.POST.get('capacity')
    status = request.POST.get('status')
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')
    try:
        cabinet = Cabinet(number=number, two_dimension_code=two_dimension, spot_id=spot_id, capacity=capacity, status=status, lat=lat, lon=lon)
        cabinet.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_cabinets()
    return HttpResponse('Success&' + html)


def cabinet_update(request, cabinet_id):
    cabinet = Cabinet.objects.filter(id=cabinet_id).first()
    spots = Spot.objects.all()
    template_name = 'hardware/cabinet/cabinet_update.html'
    context = {'cabinet': cabinet, 'spots': spots}
    response = render(request, template_name, context)
    return response


def cabinet_update_submit(request):
    number = request.POST.get('number')
    spot_id = request.POST.get('spot_id')
    two_dimension = request.POST.get('two_dimension')
    capacity = request.POST.get('capacity')
    status = request.POST.get('status')
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')

    cabinet_id = request.POST.get('cabinet_id')

    cabinet = Cabinet.objects.filter(id=cabinet_id).first()
    try:
        cabinet.number = number
        cabinet.spot_id = spot_id
        cabinet.two_dimension_code = two_dimension
        cabinet.capacity = capacity
        cabinet.status = status
        cabinet.lat = lat
        cabinet.lon = lon
        cabinet.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    return HttpResponse('Success&')


def cabinet_delete(request):
    cabinet_id = request.POST.get('cabinet_id')

    cabinet = Cabinet.objects.filter(id=cabinet_id)
    try:
        cabinet.delete()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_cabinets()
    return HttpResponse('Success&' + html)


def pole(request):
    poles = Pole.objects.all().order_by('-update_time')
    cabinets = Cabinet.objects.all().order_by('number')
    context = {'poles': poles, 'cabinets': cabinets}
    template_name = 'hardware/pole/pole.html'
    response = render(request, template_name, context)
    return response


def pole_add(request):
    number = request.POST.get('number')
    cabinet_id = request.POST.get('cabinet_id')
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_time = create_time
    try:
        pole = Pole(number=number, cabinet_id=cabinet_id, create_time=create_time, update_time=update_time)
        pole.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_poles()
    return HttpResponse('Success&' + html)


def pole_update(request, pole_id):
    pole = Pole.objects.filter(id=pole_id).first()
    cabinets = Cabinet.objects.all()
    template_name = 'hardware/pole/pole_update.html'
    context = {'pole': pole, 'cabinets': cabinets}
    response = render(request, template_name, context)
    return response


def pole_update_submit(request):
    number = request.POST.get('number')
    cabinet_number = request.POST.get('cabinet_number')
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pole_id = request.POST.get('pole_id')
    pole = Pole.objects.filter(id=pole_id).first()
    cabinet_id = Cabinet.objects.filter(number=cabinet_number).first()
    try:
        pole.number = number
        pole.cabinet_id = cabinet_id.id
        pole.update_time = update_time
        pole.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    return HttpResponse('Success&')


def pole_delete(request):
    pole_id = request.POST.get('pole_id')

    pole = Pole.objects.filter(id=pole_id)
    try:
        pole.delete()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_poles()
    return HttpResponse('Success&' + html)


def spot(request):
    template_name = 'hardware/spot/spot.html'
    spots = Spot.objects.all().order_by('province', 'city')
    rules = Rule.objects.all().order_by('-modify_time')
    context = {
        'menu_selected': 'spot_management',
        'spots': spots,
        'rules': rules
    }
    response = render(request, template_name, context)
    return response


def spot_add(request):
    spot_name = request.POST.get('spot_name')
    province = request.POST.get('province')
    city = request.POST.get('city')
    address = request.POST.get('address')
    responsible_person = request.POST.get('responsible_person')
    rule_id = request.POST.get('rule_id')

    try:
        spot = Spot(name=spot_name, province=province, city=city, address=address,
                    responsible_person=responsible_person, rule_id=rule_id)
        spot.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_spots()
    return HttpResponse('Success&' + html)


def spot_delete(request):
    spot_id = request.POST.get('spot_id')

    spot = Spot.objects.filter(id=spot_id)
    try:
        spot.delete()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    html = get_spots()
    return HttpResponse('Success&' + html)


def spot_update(request, spot_id):
    spot = Spot.objects.filter(id=spot_id).first()
    rules = Rule.objects.all().order_by('-modify_time')
    template_name = 'hardware/spot/spot_update.html'
    context = {'spot': spot, 'rules': rules}
    response = render(request, template_name, context)
    return response


def spot_update_submit(request):
    spot_name = request.POST.get('spot_name')
    province = request.POST.get('province')
    city = request.POST.get('city')
    address = request.POST.get('address')
    responsible_person = request.POST.get('responsible_person')
    rule_id = request.POST.get('rule_id')

    spot_id = request.POST.get('spot_id')

    spot = Spot.objects.filter(id=spot_id).first()
    try:
        spot.name = spot_name
        spot.province = province
        spot.city = city
        spot.address = address
        spot.responsible_person = responsible_person
        spot.rule_id = rule_id
        spot.save()
    except Exception as e:
        html = 'Fail&{0}'.format(e)
        return HttpResponse(html)

    return HttpResponse('Success&')


def get_cabinets():
    html = '<table><tr><td rowspan="2">编号</td>' \
           '<td rowspan="2">二维码</td>' \
           '<td rowspan="2">所属景区</td>' \
           '<td rowspan="2">容量</td>' \
           '<td rowspan="2">状态</td>' \
           '<td rowspan="2">经度</td>' \
           '<td rowspan="2">纬度</td>' \
           '<td colspan="2">操作</td>' \
           '</tr><tr>' \
           '<td>更新</td>' \
           '<td>删除</td></tr>'
    cabinets = Cabinet.objects.all().order_by('number')
    if cabinets:
        for cabinet in cabinets:
            spot = Spot.objects.filter(id=cabinet.spot_id).first()
            html += '<tr><td>' + cabinet.number + '</td><td>' \
                    + cabinet.two_dimension_code + '</td><td>' \
                    + spot.name + '</td><td>' \
                    + str(cabinet.capacity) + '</td><td>' \
                    + str(cabinet.status) + '</td><td>' \
                    + str(cabinet.lat) + '</td><td>' \
                    + str(cabinet.lon) + '</td>' \
                    + '<td><a href="/hardware/cabinet/cabinet_update/' + str(cabinet.id) \
                    + '">更新</a></td><td><a href="#" onclick="delete_cabinet(\'' \
                    + str(cabinet.id) +'\')">删除</a></td></tr>'

    html += '</table>'
    return html


def get_spots():
    html = '<table><tr><td rowspan="2">景点名称</td>' \
           '<td rowspan="2">省</td>' \
           '<td rowspan="2">市</td>' \
           '<td rowspan="2">详细地址</td>' \
           '<td rowspan="2">负责人</td>' \
           '<td rowspan="2">计费规则</td>' \
           '<td colspan="2">操作</td>' \
           '</tr><tr>' \
           '<td>更新</td>' \
           '<td>删除</td></tr>'
    spots = Spot.objects.all().order_by('province', 'city')
    if spots:
        for spot in spots:

            html += '<tr><td>' + spot.name + '</td><td>' \
                    + spot.province + '</td><td>' \
                    + spot.city + '</td><td>' \
                    + spot.address + '</td><td>' \
                    + spot.responsible_person + '</td><td>' \
                    + str(spot.rule_id) + '</td><td><a href="/hardware/spot/spot_update/' + str(spot.id) \
                    + '">更新</a></td><td><a href="#" onclick="delete_spot(\'' \
                    + str(spot.id) +'\')">删除</a></td></tr>'

    html += '</table>'
    return html


def get_poles():
    html = '<table><tr><td rowspan="2">编号</td>' \
           '<td rowspan="2">机柜编号</td>' \
           '<td rowspan="2">创建时间</td>' \
           '<td rowspan="2">更新时间</td>' \
           '<td colspan="2">操作</td>' \
           '</tr><tr>' \
           '<td>更新</td>' \
           '<td>删除</td></tr>'
    poles = Pole.objects.all().order_by('-update_time')
    if poles:
        for pole in poles:
            cabinet = Cabinet.objects.filter(id=pole.cabinet_id).first()
            html += '<tr><td>' + pole.number + '</td><td>' \
                    + cabinet.number + '</td><td>' \
                    + str(pole.create_time.strftime('%Y-%m-%d %H:%M:%S')) + '</td><td>' \
                    + str(pole.update_time.strftime('%Y-%m-%d %H:%M:%S')) + '</td>' \
                    + '<td><a href="/hardware/pole/pole_update/' + str(pole.id) \
                    + '">更新</a></td><td><a href="#" onclick="delete_pole(\'' \
                    + str(pole.id) +'\')">删除</a></td></tr>'

    html += '</table>'
    return html
