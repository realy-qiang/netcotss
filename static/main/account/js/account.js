$(function () {
    $.ajax({
        url: '/accountApp/account_json/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var html = '';
            $.each(data, function (key, val) {
                var status = '';
                var status_type = '';
                for (v in val) {
                    var str2 = ''
                    var date = ''
                    if (val[v].status == true) {
                        status = '开通';
                        status_type = '暂停';
                        date = val[v].pause_date
                        str2 = '<td class="td_modi">' +
                            '<input type="button" value="' + status_type + '" class="btn_start"  />' +
                            '<input type="button" value="修改" class="btn_modify" />' +
                            '<input type="button" value="删除" class="btn_delete"  /></td></tr>';
                    } else if (val[v].status == null) {
                        date = val[v].close_date;
                        status = '删除';
                        status_type = '暂停';
                        str2 = '<td></td></tr>'
                    } else if (val[v].status == false) {
                        status = '暂停';
                        status_type = '开通';
                        date = val[v].pause_date
                        str2 = '<td class="td_modi">' +
                            '<input type="button" value="' + status_type + '" class="btn_start"  />' +
                            '<input type="button" value="修改" class="btn_modify" />' +
                            '<input type="button" value="删除" class="btn_delete"  /></td></tr>';
                    }

                    if (date == null) {
                        date = ''
                    } else {
                        var year1 = date.substring(0, 4)
                        var month1 = date.substring(5, 7)
                        var day1 = date.substring(8, 10)
                        var time1 = date.substring(11, 19)
                    }
                    var year = val[v].create_date.substring(0, 4)
                    var month = val[v].create_date.substring(5, 7)
                    var day = val[v].create_date.substring(8, 10)
                    var time = val[v].create_date.substring(11, 19)
                    var str1 = '<tr><td>' + val[v].id + '</td><td class="userInfo" style="color: dodgerblue">' + val[v].real_name + '</td>' +
                        '<td>' + val[v].idcard_no + '</td><td>' + val[v].login_name + '</td><td>' + status +
                        '</td><td style="width: 150px">' + year + '年' + month + '月' + day + '日 ' + time + '</td><td>' + year1 + '年' + month1 + '月' + day1 + '日 ' + time1 + '</td>' + str2;
                    html += str1
                }
                ;
            });
            $('#first_tr').after(html);
            changStatus()
        }
    });
    $('.btn_add').click(function () {
        window.open('/accountApp/account_add/', target = '_self')
    });
    $('.btn_search').click(function () {
        var idcard = $('#id_search').val();
        var real_name = $('#real_search').val();
        var login_name = $('#login_search').val();
        var status = $('.select_search').val();
        // console.log(idcard,real_name,login_name,status);
        $.ajax({
            url: '/accountApp/account_json/',
            type: 'POST',
            data: {'idcard': idcard, 'real_name': real_name, 'login_name': login_name, 'status': status},
            dataType: 'json',
            success: function (data) {
                var html = '';

                $.each(data, function (key, val) {
                    var status = '';
                    var status_type = '';
                    for (v in val) {
                        var str3 = ''
                        var date = ''
                        if (val[v].status == true) {
                            status = '开通';
                            status_type = '暂停';
                            date = val[v].pause_date
                            str3 = '<td class="td_modi">' +
                                '<input type="button" value="' + status_type + '" class="btn_start"  />' +
                                '<input type="button" value="修改" class="btn_modify" />' +
                                '<input type="button" value="删除" class="btn_delete"  /></td></tr>'
                        } else if (val[v].status == null) {
                            date = val[v].close_date;
                            status = '删除';
                            status_type = '暂停';
                        } else if (val[v].status == false) {
                            status = '暂停';
                            status_type = '开通';
                            date = val[v].pause_date;
                            str3 = '<td class="td_modi">' +
                                '<input type="button" value="' + status_type + '" class="btn_start"  />' +
                                '<input type="button" value="修改" class="btn_modify" />' +
                                '<input type="button" value="删除" class="btn_delete"  /></td></tr>'
                        }
                        if (date == null) {
                            date = ''
                        }
                        var str1 = '<tr><td>' + val[v].id + '</td><td class="userInfo" style="color: dodgerblue">' + val[v].real_name + '</td>' +
                            '<td>' + val[v].idcard_no + '</td><td>' + val[v].login_name + '</td><td>' + status +
                            '</td><td>' + val[v].create_date + '</td><td>' + date + '</td>' + str3;
                        html += str1
                    }
                    ;
                });
                $('#first_tr').nextAll().html('');
                $('#first_tr').after(html);
                changStatus();
            }
        });
    });

    $('#fee').click(function () {
        window.open('/tariffApp/feeList/', target = '_self')
    });

    $('#service').click(function () {
        window.open('/serviceApp/serviceList/', target = '_self');
    });

});

function changStatus() {
    $(".btn_start").click(function () {
        var r = window.confirm("确定要开通或暂停此账务账号吗？");
        if (!r) {
            return
        }
        var $id = $(this).parent().parent().children();
        var id = $id.html();
        var status = $(this).val();
        var status_type;
        if (status == '开通') {
            status_type = 1
        } else {
            status_type = 0
        }
        $.ajax(
            {
                url: '/accountApp/change_status/',
                type: "GET",
                data: {'id': id, 'status_type': status_type},
                dataType: 'json',
                success: function (data) {
                    if (data['account_status'] == true) {
                        $td = $id.next().next().next().next();
                        $td.html('开通');
                        $td.next().html(data['create_date']);
                        $td.next().next().html(data['pause_date']);
                        $td.next().next().next().html(
                            '<input type="button" value="暂停" class="btn_start"  />' +
                            '<input type="button" value="修改" class="btn_modify" />' +
                            '<input type="button" value="删除" class="btn_delete"  />');

                    } else if (data['account_status'] == false) {
                        $td = $id.next().next().next().next();
                        $td.html('暂停');
                        $td.next().html(data['create_date']);
                        $td.next().next().html(data['pause_date']);
                        $td.next().next().next().html(
                            '<input type="button" value="开通" class="btn_start"  />' +
                            '<input type="button" value="修改" class="btn_modify" />' +
                            '<input type="button" value="删除" class="btn_delete"  />');
                    }
                    changStatus()


                }
            })
    });
    $('.btn_delete').click(function () {
        // deleteAccount()
        var r = window.confirm("确定要删除此账务账号吗？\r\n删除后将不能恢复，且会删除其下属的所有业务账号。");
        if (!r) {
            return
        }
        var $id = $(this).parent().parent().children();
        var id = $id.html();
        var status_type;
        console.log(status_type)
        $.ajax({
            url: '/accountApp/change_status/',
            type: "GET",
            data: {'id': id, 'status_type': status_type},
            dataType: 'json',
            success: function (data) {
                $td = $id.next().next().next().next();
                $td.html('删除');
                $td.next().html(data['create_date']);
                $td.next().next().html(data['close_date']);
                $td.next().next().next().html('');
            }
        })

    });
    $('.btn_modify').click(function () {
        var $id = $(this).parent().parent().children();
        var id = $id.html();
        window.open('/accountApp/account_modi/?id=' + id, target = "_self")

    });
    $('.userInfo').click(function () {
        var id = $(this).parent().children().html();
        console.log(id);
        window.open('/accountApp/account_detail/?id=' + id, target = '_self')

    })
}
