from django.conf.urls import url

from accountApp import views

urlpatterns =[
    url(r'^accountList/', views.accountList, name='accountList'),
    url(r'^account_add/', views.account_add, name='account_add'),
    url(r'^account_json/',views.AccountView.as_view()),
    # url(r'^account_json/',views.AccountView.as_view()),

    # 保存
    url(r'^account_save/',views.account_save),
   #状态
    url(r'^change_status/',views.change_status),
    #修改
    url(r'^account_modi/',views.account_modi),
    url(r'^account_detail/',views.account_detail,),

]