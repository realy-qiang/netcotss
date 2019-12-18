from django.conf.urls import url

from serviceApp import views

urlpatterns = [
    # 展示所有数据库信息
    url(r'^serviceList/', views.serviceList, name='serviceList'),
    # 跳转到添加页面
    url(r'^toServiceAdd/', views.toServiceAdd, name='toServiceAdd'),
    # 添加功能实现
    url(r'^serviceAdd/', views.serviceAdd, name='serviceAdd'),
    # 跳转到修改页面
    url(r'^toServiceModi/', views.toServiceModi, name='toServiceModi'),
    # 修改功能实现
    url(r'^serviceModi/', views.serviceModi, name='serviceModi'),
    # 跳转到详情页面
    url(r'serviceDetial/', views.serviceDetial, name='serviceDetial'),
    # 添加页面，身份证信息查询
    url(r'^search_idCard/', views.serch_idCard, name='search_idCard'),
    # 判断是否保存成功,判断host下os账号是否已经存在
    url(r'^is_save_sure/', views.is_save_sure, name='is_save_sure'),
    # 删除功能实现
    url(r'^serviceDel/', views.serviceDel, name='serviceDel'),
    # 暂停和开通功能实现
    url(r'^serviceSet/', views.serviceSet, name='serviceSet'),
    # 联合查询
    url(r'^serviceSearch/', views.serviceSearch, name='serviceSearch')

]