import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from accountApp.models import Account
from accountApp.serializers import accountSerializer

#
def accountList(request):
    return render(request, 'main/account/account_list.html')


#
# def account_add(request):
#     return render(request, 'main/account/account_add.html')


class AccountView(View):
    def get(self,request):
        accounts = Account.objects.all()
        accountsserializer = accountSerializer(accounts,many=True)
        print(accountsserializer.data)
        data = {
            'accounts':accountsserializer.data
        }
        return JsonResponse(data=data)
    def post(self,request):
        idcard = request.POST.get('idcard')
        status = request.POST.get('status')
        real_name = request.POST.get('real_name')
        login_name = request.POST.get('login_name')
        data = {}
        if status == '0':
            accounts = Account.objects.all()
            if idcard :
                accounts_id = accounts.filter(idcard_no=idcard)
                if accounts_id.count() > 0:
                    if real_name:
                        account_name = accounts_id.filter(real_name=real_name)
                        if account_name.count() > 0:
                            accountserializer = accountSerializer(account_name,many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_id.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_id, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if real_name:
                accounts_real = accounts.filter(real_name=real_name)
                if accounts_real.count() > 0:
                    if idcard:
                        accounts_id = accounts_real.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_real.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_real, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if login_name:
                accounts_login = accounts.filter(login_name=login_name)
                if accounts_login.count() > 0:
                    if idcard:
                        accounts_id = accounts_login.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if real_name:
                        account_real = accounts_login.filter(real_name=real_name)
                        if account_real.count() > 0:
                            accountserializer = accountSerializer(account_real, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_login, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            accountserializer = accountSerializer(accounts, many=True)
            data['account_list'] = accountserializer.data
            return JsonResponse(data=data)
        if status == 'True':
            accounts = Account.objects.filter(status=True)
            if idcard:
                accounts_id = accounts.filter(idcard_no=idcard)
                if accounts_id.count() > 0:
                    if real_name:
                        account_name = accounts_id.filter(real_name=real_name)
                        if account_name.count() > 0:
                            accountserializer = accountSerializer(account_name, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_id.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_id, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if real_name:
                accounts_real = accounts.filter(real_name=real_name)
                if accounts_real.count() > 0:
                    if idcard:
                        accounts_id = accounts_real.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_real.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_real, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if login_name:
                accounts_login = accounts.filter(login_name=login_name)
                if accounts_login.count() > 0:
                    if idcard:
                        accounts_id = accounts_login.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if real_name:
                        account_real = accounts_login.filter(real_name=real_name)
                        if account_real.count() > 0:
                            accountserializer = accountSerializer(account_real, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_login, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            accountserializer = accountSerializer(accounts, many=True)
            data['account_list'] = accountserializer.data
            return JsonResponse(data=data)
        if status =='False':
            accounts = Account.objects.filter(status=False)
            if idcard:
                accounts_id = accounts.filter(idcard_no=idcard)
                if accounts_id.count() > 0:
                    if real_name:
                        account_name = accounts_id.filter(real_name=real_name)
                        if account_name.count() > 0:
                            accountserializer = accountSerializer(account_name, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_id.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_id, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if real_name:
                accounts_real = accounts.filter(real_name=real_name)
                if accounts_real.count() > 0:
                    if idcard:
                        accounts_id = accounts_real.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_real.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_real, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if login_name:
                accounts_login = accounts.filter(login_name=login_name)
                if accounts_login.count() > 0:
                    if idcard:
                        accounts_id = accounts_login.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if real_name:
                        account_real = accounts_login.filter(real_name=real_name)
                        if account_real.count() > 0:
                            accountserializer = accountSerializer(account_real, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_login, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            accountserializer = accountSerializer(accounts, many=True)
            data['account_list'] = accountserializer.data
            return JsonResponse(data=data)
        if status == 'Null':
            accounts = Account.objects.filter(status=None)
            if idcard:
                accounts_id = accounts.filter(idcard_no=idcard)
                if accounts_id.count() > 0:
                    if real_name:
                        account_name = accounts_id.filter(real_name=real_name)
                        if account_name.count() > 0:
                            accountserializer = accountSerializer(account_name, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_id.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_id, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if real_name:
                accounts_real = accounts.filter(real_name=real_name)
                if accounts_real.count() > 0:
                    if idcard:
                        accounts_id = accounts_real.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if login_name:
                        account_login = accounts_real.filter(login_name=login_name)
                        if account_login.count() > 0:
                            accountserializer = accountSerializer(account_login, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_real, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            if login_name:
                accounts_login = accounts.filter(login_name=login_name)
                if accounts_login.count() > 0:
                    if idcard:
                        accounts_id = accounts_login.filter(idcard_no=idcard)
                        if accounts_id.count() > 0:
                            accountserializer = accountSerializer(accounts_id, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)

                    if real_name:
                        account_real = accounts_login.filter(real_name=real_name)
                        if account_real.count() > 0:
                            accountserializer = accountSerializer(account_real, many=True)
                            data['account_list'] = accountserializer.data
                            return JsonResponse(data=data)
                        else:
                            return JsonResponse(data=data)
                    else:
                        accountserializer = accountSerializer(accounts_login, many=True)
                        data['account_list'] = accountserializer.data
                        return JsonResponse(data=data)
                else:
                    return JsonResponse(data=data)
            accountserializer = accountSerializer(accounts, many=True)
            data['account_list'] = accountserializer.data
            return JsonResponse(data=data)
        return JsonResponse(data=data)



def account_add(request):
    return render(request, 'main/account/account_add.html')
def account_save(request):
        idcard = request.POST.get('idcard')
        accounts = Account.objects.filter(idcard_no=idcard)
        data ={}
        if accounts.count() > 0 :
            data['status'] = 201
        else:
            new_account = Account()
            data['status'] = 200
            login_name = request.POST.get('login_name')
            login_passwd = request.POST.get('login_passwd')
            real_name = request.POST.get('real_name')
            telephone = request.POST.get('telephone')
            recommender_id = request.POST.get('recommender_id')
            birthdate = request.POST.get('birthdate')
            email = request.POST.get('email')
            occupation = request.POST.get('occupation')
            gender = request.POST.get('gender')
            mailaddress = request.POST.get('mailaddress')
            zipcode = request.POST.get('zipcode')
            qq = request.POST.get('qq')

            new_account.real_name = real_name
            new_account.idcard_no = idcard
            new_account.login_name = login_name
            new_account.login_passwd = login_passwd
            new_account.telephone = telephone
            new_account.birthdate = birthdate
            new_account.recommender_id = recommender_id
            new_account.email = email
            new_account.occupation = occupation
            new_account.gender = gender
            new_account.mailaddress = mailaddress
            new_account.zipcode = zipcode
            new_account.qq = qq
            new_account.save()

        return JsonResponse(data=data)


def change_status(request):
    if request.method == "GET":
        data = {
            'msg':'ok',
            'status':200,
        }
        status_type = request.GET.get('status_type')
        id = request.GET.get('id')
        if status_type == '1':
            account_id = Account.objects.get(pk=id)
            account_id.status =  True
            account_id.pause_date = None
            account_id.save()
            data['account_status'] = account_id.status
            data['create_date']=account_id.create_date
            data['pause_date'] = account_id.pause_date
        if status_type == '0':
            account_id = Account.objects.get(pk=id)
            account_id.status = False
            account_id.pause_date = time.strftime("%Y-%m-%d %X", time.localtime())
            account_id.save()
            data['account_status'] = account_id.status
            data['create_date'] = account_id.create_date
            data['pause_date'] = account_id.pause_date
        if status_type == None:
            account_id = Account.objects.get(pk=id)
            account_id.status = None
            account_id.close_date = time.strftime("%Y-%m-%d %X", time.localtime())
            account_id.save()
            data['account_status'] = account_id.status
            data['create_date'] = account_id.create_date
            data['close_date'] = account_id.close_date
        return JsonResponse(data=data)


def account_modi(request):
    return render(request,'main/account/account_modi.html')


def account_detail(request):

    return render(request,'main/account/account_detail.html')