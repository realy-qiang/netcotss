$(function () {
    $('#cost_name').blur(function () {

        var cost_name = $('#cost_name').val()
        alert(cost_name)
        $.getJSON('/tariffApp/type_is_exit/',
            {'cost_name':cost_name},
            function (data) {
                if(data['status'] == 200){
                    alert(11111)
                    $('#cost_validate_msg_short').html('资费名称存在')
                }else {
                    $('#cost_validate_msg_short').html('资费名称不存在, 请重新输入')
                }
            })
        // cost_validate_msg_short
    })

    $('#fee_add_back').click(function () {
        window.location.href = '/tariffApp/feeList/'
    })
})

//保存结果的提示
function showResult() {
    showResultDiv(true);
    window.setTimeout("showResultDiv(false);", 3000);
}

function showResultDiv(flag) {
    var divResult = document.getElementById("save_result_info");
    if (flag)
        divResult.style.display = "block";
    else
        divResult.style.display = "none";
}


function parse1() {
    var cost_name = $('#cost_name').val();
    var cost_type = $('input[name=radFeeType]:checked').val();
    var bast_duration = $('#bast_duration').val();
    var base_cost = $('#base_cost').val();
    var unit_cost = $('#unit_cost').val();
    var descr = $('#descr').val();

    if (cost_type == '包月') {
        if (cost_name.trim() == '' || base_cost.trim() == '' || descr.trim() == '') {
            return false
        } else {
            return true
        }
    } else if (cost_type == '计时') {
        if (cost_name.trim() == '' || unit_cost.trim() == '' || descr.trim() == '') {
            return false
        } else {
            return true
        }
    } else {
        if (cost_name.trim() == '' || bast_duration.trim() == '' || base_cost.trim() == '' || unit_cost.trim() == '' || descr.trim() == '') {
            return false
        } else {
            return true
        }
    }

}


//切换资费类型
function feeTypeChange(type) {
    alert(type)
    if (type == 1) {
        $('#bast_duration').attr('readonly', true)
        $('#unit_cost').attr('readonly', true)
        $('#base_cost').attr('readonly', false)
    }else if (type == 2) {
        $('#unit_cost').attr('readonly', false)
        $('#bast_duration').attr('readonly', false)
        $('#base_cost').attr('readonly', false)
    } else if (type == 3) {
        $('#unit_cost').attr('readonly', false)
        $('#bast_duration').attr('readonly', true)
        $('#base_cost').attr('readonly', true)
    }
}
