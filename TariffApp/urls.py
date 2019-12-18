from django.conf.urls import url

from TariffApp import views

urlpatterns = [
    url(r'^feeList/', views.feeList, name='feeList'),
    url(r'^getFee/', views.getFee, name='getFee'),
    url(r'^toModify/', views.toModify, name='toModify'),
    url(r'^modify/', views.modify, name='modify'),
    # 启用
    url(r'^startUp/', views.startUp, name='startUp'),
    # 增加页面
    url(r'^toAddFee/', views.toAddFee, name='toAddFee'),
    # 增加功能
    url(r'^addFee', views.addFee, name='addFee'),
    # 删除功能
    url(r'^deleteFee/', views.deleteFee, name='deleteFee'),
    # 详情信息页
    url(r'^detailFee/', views.detailFee, name='detailFee'),

    # 判断资费类型是否存在
    url(r'^type_is_exit/', views.type_is_exit),
    # # # 根据时长排序
    url(r'^orderByTime/', views.orderByTime, name='orderByTime'),
    # 根据基费用排序
    url(r'^orderByCost/', views.orderByCost, name='orderByCost'),
    # 根据单位费用排序
    url(r'^orderUnitCost/', views.orderUnitCost, name='orderUnitCost')
]