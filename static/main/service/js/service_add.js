$(function () {
    // 添加页面查询按钮
    $('.btn_search_large').click(function () {
        var idcard_no = $('#idcard_no').val()
        $.getJSON(
            '/serviceApp/search_idCard/',
            {'idcard_no': idcard_no},
            function (data) {
                if (data['status'] == 200) {
                    $('#account_id').val(data['account_id'])
                    $('#service_save').attr('disabled', false)
                } else {
                    $('.validate_msg_short').html('没有此身份证号，请重新录入。')

                }
            }
        )
    });

    $('#host').blur(function () {
        var host = $(this).val()
        var reg = /^(2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2}$/;
        if (reg.test(host)) {
            $('.host_validate_msg').html('符合IP的地址规范')
            $('#service_save').attr('disabled', false)
        } else {
            $('.host_validate_msg').html('不符合IP的地址规范')
        }
    });

    $('#os_name').blur(function () {
        var os_name = $(this).val()
        var host = $('#host').val();
        var reg = /^[0-9A-Za-z_]{1,8}$/;
        if (reg.test(os_name)) {
            $('.os_name_validate_msg').html('格式正确')
            $.getJSON(
            '/serviceApp/is_save_sure/',
            {'host':host, 'os_name':os_name},
            function a(data) {
                if(data['status'] == 200){
                    $('#save_result_info').text(host+'服务器上已经开通过 OS 账号'+os_name)
                    $('#service_save').attr('disabled', true)
                }else {
                    $('#service_save').attr('disabled', false)
                }
            });
        } else {
            $('.os_name_validate_msg').html('格式不正确')
        }

    })

    $('#password').blur(function () {
        var password = $(this).val()
        var reg = /^[0-9A-Za-z_]{8,30}$/;
        if (reg.test(password)) {
            $('.password_validate_msg_long').html('密码格式正确')
        } else {
            $('.password_validate_msg_long').html('密码格式不正确')
        }
    })

    $('#password_sure').blur(function () {
        var password_sure = $(this).val()
        var password = $('#password').val()
        if (password == password_sure) {
            $('.password_sure_validate_msg').html('密码正确')
        } else {
            $('.password_sure_validate_msg').html('两次密码不一致，请重新输入')
        }
    })

    $('#addService_quit').click(function () {
        window.location.href = '/serviceApp/serviceList'
    })
})

function parse() {
    var idcard_no = $('#idcard_no').val();
    var account_id = $('#account_id').val();
    var host = $('#host').val();
    var os_name = $('#os_name').val();
    var password = $('#password').val();
    var password_sure = $('#password_sure').val();


    if (idcard_no.trim() == '' || account_id.trim() == '' || host.trim() == '' || os_name.trim() == '' || password.trim() == '' || password_sure.trim() == '') {
        return false
    } else {
        alert('保存成功')
        return true
    }

}