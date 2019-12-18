$(function () {
    $('.btn_add').click(function () {
        window.location.href = '/serviceApp/toServiceAdd/'
    });



    $('#search').click(function () {
        var os_name = $('#os_name').val()
        var host = $('#host').val()
        var idcard_no = $('#idcard_no').val()
        var service_type = $('#service_type').val()

        window.location.href = '/serviceApp/serviceSearch/?os_name='+os_name+'&host='+host+'&idcard_no='+idcard_no+'&service_type='+service_type
    })

});

//显示角色详细信息
function showDetail(flag, a) {
    var detailDiv = a.parentNode.getElementsByTagName("div")[0];
    if (flag) {
        detailDiv.style.display = "block";
    } else
        detailDiv.style.display = "none";
}

//删除
function deleteAccount(service_id) {
    var r = window.confirm("确定要删除此业务账号吗？删除后将不能恢复。");
    if(r){
        $.getJSON(
            '/serviceApp/serviceDel',
            {'service_id':service_id},
            function (data) {
                document.getElementById("delete_result_info").style.display = "block";
                window.location.href = '/serviceApp/serviceList/'
            }
        )

    }

}

//开通或暂停
function setState(obj, service_id) {
    if (obj.valueOf() == false){
        var r = window.confirm("确定要暂停此业务账号吗？");
    }else {
        var r = window.confirm("确定要开通此业务账号吗？");

    }


    if(r){
        $.getJSON(
            '/serviceApp/serviceSet',
            {'service_id':service_id},
            function (data) {
                if (data['service_status'] == false ){
                    document.getElementById("operate_result_info").style.display = "block";

                }else {
                    document.getElementById("pause_result_info").style.display = "block";
                }

                window.location.href = '/serviceApp/serviceList/'
            }
        )}
    // document.getElementById("operate_result_info").style.display = "block";
}

function modifi(service_id) {
    window.location.href = '/serviceApp/toServiceModi/?service_id='+service_id
}
