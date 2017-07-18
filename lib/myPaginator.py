from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


def pagintor(request, data_list):
    limit = 1

    paginator = Paginator(data_list, limit)

    page = request.GET.get('page')

    try:
        data_list = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data_list = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return data_list
