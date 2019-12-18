import time

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from TariffApp.models import Cost, UserCost
from accountApp.models import Account
from serviceApp.models import Service


def serviceList(request):

    service_list = Service.objects.all()

    paginator = Paginator(service_list, 3)
    page = int(request.GET.get('page', 1))
    service_list = paginator.page(page)

    pages = paginator.page_range

    account = Account.objects.all()

    context = {
        'service_list': service_list,
        'pages': pages,
        'page': page,
        'account':account
    }

    return render(request, 'main/service/service_list.html', context=context)


def serviceAdd(request):
    account_id = request.POST.get('account_id')
    host = request.POST.get('host')
    os_name = request.POST.get('os_name')
    password = request.POST.get('password')
    cost_type = request.POST.get('type')

    cost = Cost.objects.get(name=cost_type.replace(' ', ''))

    usercost = UserCost()
    usercost.name = cost_type.replace(' ', '')
    usercost.base_duration = cost.base_duration
    usercost.base_cost = cost.base_cost
    usercost.unit_cost = cost.unit_cost
    usercost.status = False
    usercost.descr = cost.descr
    usercost.creatime = time.strftime("%Y-%m-%d %X", time.localtime())
    usercost.cost_type = '0'

    usercost.save()

    service = Service()

    this_usercost = UserCost.objects.last()

    service.s_account_id = account_id
    service.unix_host = host
    service.os_username = os_name
    service.login_passwd = password
    service.status = True
    service.create_date = time.strftime("%Y-%m-%d %X", time.localtime())
    service.s_usercost_id = this_usercost.id
    service.save()

    return redirect(reverse('serviceApp:serviceList'))


def serch_idCard(request):
    input_idcard_no = request.GET.get('idcard_no')

    data = {
        'msg': 'ok',
        'status': 200
    }

    account = Account.objects.filter(idcard_no=input_idcard_no)
    if account.exists():
        account = Account.objects.get(idcard_no=input_idcard_no)
        data['account_id'] = account.id
        return JsonResponse(data=data)
    else:
        data['msg'] = '没有此身份证号，请重新输入'
        data['status'] = 201
        return JsonResponse(data=data)



def toServiceAdd(request):
    return render(request, 'main/service/service_add.html')


def toServiceModi(request):
    service_id = request.GET.get('service_id')

    service = Service.objects.get(pk=service_id)

    context = {
        'service': service
    }

    return render(request, 'main/service/service_modi.html', context=context)


def serviceModi(request):
    service_id = request.GET.get('service_id')

    cost_type = request.POST.get('cost_type')

    service = Service.objects.get(pk=service_id)

    time.sleep(60)
    service.s_usercost.name = cost_type

    return redirect(reverse('serviceApp:serviceList'))

# 详情页面
def serviceDetial(request):
    service_id = request.GET.get('service_id')

    service = Service.objects.get(pk=service_id)

    context = {
        'service': service
    }

    return render(request, 'main/service/service_detail.html', context=context)

# 是否保存成功
def is_save_sure(request):
    host = request.GET.get('host')
    os_name = request.GET.get('os_name')

    services = Service.objects.filter(unix_host=host).filter(os_username=os_name)

    data = {
        'msg': 'ok',
        'status': 200
    }

    if services.count() > 0:
        return JsonResponse(data=data)
    else:
        data['msg'] = '保存失败'
        data['status'] = 201
        return JsonResponse(data=data)

# 删除操作
def serviceDel(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(pk=service_id)

    service.status = None
    service.close_date = time.strftime("%Y-%m-%d %X", time.localtime())

    service.save()
    data = {
        'msg': 'ok',
        'status': 200
    }
    return JsonResponse(data=data)

# 暂停和开通操作
def serviceSet(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(pk=service_id)

    if service.status:
        service.status = False
        service.pause_date = time.strftime("%Y-%m-%d %X", time.localtime())
    else:
        service.status = True
        service.pause_date = None

    service.save()

    data = {
        'msg': 'ok',
        'status': 200,
        'service_status': service.status
    }
    return JsonResponse(data=data)

# 联合查询
def serviceSearch(request):
    os_name = request.GET.get('os_name')
    host = request.GET.get('host')
    idcard_no = request.GET.get('idcard_no')
    service_type = request.GET.get('service_type')

    service = Service.objects.all()

    if service_type == '暂停':
        service = service.filter(status=False)
    elif service_type == '删除':
        service = service.filter(status=None)
    elif service_type == '开通':
        service = service.filter(status=True)

    if idcard_no:
        account = Account.objects.filter(idcard_no=idcard_no)
        if account.count() > 0:
            account_id = account[0].id
            service = service.filter(s_account_id=account_id)
        else:
            service.filter(s_account_id=None)


        if os_name:
            service = service.filter(os_username=os_name)

            if host:
                service = service.filter(unix_host=host)
                if idcard_no:
                    service.filter()
            else:
                service = service
        else:
            if host:
                service = service.filter(unix_host=host)
            else:
                service = service

    else:
        service = service

        if os_name:
            service = service.filter(os_username=os_name)

            if host:
                service = service.filter(unix_host=host)
                if idcard_no:
                    service.filter()
            else:
                service = service
        else:
            if host:
                service = service.filter(unix_host=host)
            else:
                service = service

    context = {
        'service_list': service
    }
    return render(request, 'main/service/service_list.html', context=context)
