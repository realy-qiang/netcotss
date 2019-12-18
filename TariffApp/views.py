from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import time

# Create your views here.
from django.urls import reverse

from TariffApp.models import Cost, UserCost


# 资费列表
def feeList(request):

    # return render(request, 'index.html')
    # 排序功能
    # is_order = request.GET.get('order')
    # if is_order == 'time':
    #     order_time = request.GET.get('orderBy')
    #     order_base_cost = 'sort_asc'
    #     order_unit_cost = 'sort_asc'
    #     if order_time == 'sort_asc':
    #         costs = UserCost.objects.order_by('base_duration')
    #         order_time = 'sort_asc'
    #     else:
    #         costs = UserCost.objects.order_by('-base_duration')
    #         order_time = 'sort_desc'
    # elif is_order == 'BaseCost':
    #     order_base_cost = request.GET.get('orderBy')
    #     order_time = 'sort_asc'
    #     order_unit_cost = 'sort_asc'
    #     if order_base_cost == 'sort_asc':
    #         costs = UserCost.objects.order_by('base_cost')
    #         order_base_cost = 'sort_asc'
    #     else:
    #         costs = UserCost.objects.order_by('-base_cost')
    #         order_base_cost = 'sort_desc'
    # elif is_order == 'UnitCost':
    #     order_unit_cost = request.GET.get('orderBy')
    #     order_time = 'sort_asc'
    #     order_base_cost = 'sort_asc'
    #     if order_unit_cost == 'sort_asc':
    #         costs = UserCost.objects.order_by('-base_cost')
    #         order_unit_cost = 'sort_asc'
    #     else:
    #         costs = UserCost.objects.order_by('base_cost')
    #         order_unit_cost = 'sort_desc'
    # else:
    costs = UserCost.objects.all()
    order_unit_cost = 'sort_asc'
    order_time = 'sort_asc'
    order_base_cost = 'sort_asc'

    paginator = Paginator(costs, 3)
    page = int(request.GET.get('page', 1))
    costs = paginator.page(page)
    pages = []
    for p in range(1, paginator.num_pages + 1):
        pages.append(p)

    flag = True
    for cost in costs:
        if not cost.status:
            flag = False

    print(order_base_cost, order_time, order_unit_cost)
    context = {
        'costs': costs,
        'flag': flag,
        'pages': pages,
        'page': page,
        'order_baseCost': order_base_cost,
        'order_time': order_time,
        'order_unitCost': order_unit_cost,
    }
    return render(request, 'main/fee/fee_list.html', context=context)


def getFee(request):
    costs = UserCost.objects.all()
    return render(request, 'main/fee/fee_list.html', context=locals())


# 修改页面
def toModify(request):
    id = request.GET.get('id')
    return render(request, 'main/fee/fee_modi.html', context=locals())


# 修改功能实现
def modify(request):
    id = request.POST.get('id')
    cost = UserCost.objects.get(pk=id)

    name = request.POST.get('name')
    radFeeType = request.POST.get('radFeeType')
    print(radFeeType)
    base_duration = request.POST.get('base_duration')
    base_cost = request.POST.get('base_cost')
    unit_cost = request.POST.get('unit_cost')
    descr = request.POST.get('descr')

    if radFeeType == '套餐':
        cost.name = name
        cost.base_duration = base_duration
        cost.base_cost = base_cost
        cost.unit_cost = unit_cost
    elif radFeeType == '包月':
        cost.name = radFeeType
        cost.base_duration = None
        cost.base_cost = base_cost
        cost.unit_cost = None
    else:
        cost.name = radFeeType
        cost.base_duration = None
        cost.base_cost = None
        cost.unit_cost = unit_cost

    cost.descr = descr

    cost.save()

    return redirect(reverse('tariffApp:feeList'))


# 启用功能实现
def startUp(request):
    id = request.GET.get('id')
    print(id)
    cost = UserCost.objects.get(pk=id)
    cost.startime = time.strftime("%Y-%m-%d %X", time.localtime())
    cost.status = True
    cost.save()

    return redirect(reverse('tariffApp:feeList'))


# 添加页面
def toAddFee(request):
    return render(request, 'main/fee/fee_add.html')


# 添加功能实现
def addFee(request):
    cost = UserCost()
    name = request.POST.get('name')
    radFeeType = request.POST.get('radFeeType')
    base_duration = request.POST.get('bast_duration')
    print(base_duration)

    base_cost = request.POST.get('base_cost')
    unit_cost = request.POST.get('unit_cost')
    descr = request.POST.get('descr')

    if radFeeType == '套餐':
        cost.name = name
        cost.base_duration = base_duration
        cost.base_cost = base_cost
        cost.unit_cost = unit_cost
    elif radFeeType == '包月':
        cost.name = radFeeType
        cost.base_duration = None
        cost.base_cost = base_cost
        cost.unit_cost = None
    else:
        cost.name = radFeeType
        cost.base_duration = None
        cost.base_cost = None
        cost.unit_cost = unit_cost

    cost.status = False
    cost.creatime = time.strftime("%Y-%m-%d %X", time.localtime())
    cost.descr = descr

    cost.save()
    return redirect(reverse('tariffApp:feeList'))


# 删除功能实现
def deleteFee(request):
    id = request.GET.get('id')
    print(id)
    cost = UserCost.objects.get(pk=id)
    cost.delete()

    return redirect(reverse('tariffApp:feeList'))


# 详情页面
def detailFee(request):
    id = request.GET.get('id')
    cost = UserCost.objects.get(pk=id)
    context = {
        'cost': cost
    }
    return render(request, 'main/fee/fee_detail.html', context=context)


# 时间排序
def orderByTime(request):
    order = request.GET.get('orderBy')
    print(order)
    if order == 'sort_asc':
        costs = UserCost.objects.order_by('base_duration')
    else:
        costs = UserCost.objects.order_by('-base_duration')
    paginator = Paginator(costs, 3)
    page = int(request.GET.get('page', 1))
    costs = paginator.page(page)
    pages = paginator.page_range

    flag = True
    for cost in costs:
        if not cost.status:
            flag = False
    context = {
        'costs': costs,
        'flag': flag,
        'pages': pages,
        'page': page,
        'order_baseCost': 'sort_asc',
        'order_time': order,
        'order_unitCost': 'sort_asc'
    }
    return render(request, 'main/fee/fee_list.html', context=context)


#
#
# 基本费用排序
def orderByCost(request):
    order = request.GET.get('orderBy')
    if order == 'sort_asc':
        costs = UserCost.objects.order_by('base_cost')
    else:
        costs = UserCost.objects.order_by('-base_cost')
    paginator = Paginator(costs, 3)
    page = int(request.GET.get('page', 1))
    costs = paginator.page(page)
    pages = paginator.page_range

    flag = True
    for cost in costs:
        if not cost.status:
            flag = False
    context = {
        'costs': costs,
        'flag': flag,
        'pages': pages,
        'page': page,
        'order_baseCost': order,
        'order_time': 'sort_asc',
        'order_unitCost': 'sort_asc'
    }
    return render(request, 'main/fee/fee_list.html', context=context)


#
#
# 单位费用排序
def orderUnitCost(request):
    order = request.GET.get('orderBy')
    if order == 'sort_asc':
        costs = UserCost.objects.order_by('-unit_cost')
    else:
        costs = UserCost.objects.order_by('unit_cost')
    paginator = Paginator(costs, 3)
    page = int(request.GET.get('page', 1))
    costs = paginator.page(page)
    pages = paginator.page_range

    flag = True
    for cost in costs:
        if not cost.status:
            flag = False
    context = {
        'costs': costs,
        'flag': flag,
        'pages': pages,
        'page': page,
        'order_baseCost': 'sort_asc',
        'order_time': 'sort_asc',
        'order_unitCost': order,
    }
    return render(request, 'main/fee/fee_list.html', context=context)


def type_is_exit(request):
    type_name = request.GET.get('cost_name')

    cost = Cost.objects.filter(name=type_name)

    data = {
        'msg': 'ok',
        'status': 200,
    }

    if cost.count() > 0:
        return JsonResponse(data=data)
    else:
        data['status'] = 201
        return JsonResponse(data=data)
