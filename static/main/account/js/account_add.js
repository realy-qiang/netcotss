//保存成功的提示信息
function showResult() {
    var real_name = $('#name').val();
    var idcard = $('#idcard').val();
    var login_name = $('#login_name').val();
    var login_passwd = $('#Password1').val();
    var telephone = $('#telephone').val();
    var recommender_id = $('#recommender_id').val();
    var birthdate = $('#birthdate').val();
    var email = $('#email').val();
    var occupation = $('#occupation').val();
    var gender = $('input[name="radSex"]:checked').val();
    var mailaddress = $('#mailaddress').val();
    var zipcode = $('#zipcode').val();
    var qq = $('#qq').val();
    if(real_name.length ==0 || idcard.length==0 || login_name.length==0||login_passwd.length==0||telephone.length==0){
        $('#save_result_info').text('提示：请输入完整的信息');
        showResultDiv(true);
        window.setTimeout("showResultDiv(false);", 3000);
    }else {
        $.ajax({
            url:'/accountApp/account_save/',
            data:{'idcard':idcard,
                'login_passwd':login_passwd,
                'login_name':login_name,
                'real_name':real_name,
                'telephone':telephone,
                'recommender_id':recommender_id,
                'birthdate':birthdate,
                'email':email,
                'occupation':occupation,
                'gender':gender,
                'mailaddress':mailaddress,
                'zipcode':zipcode,
                'qq':qq,
            },
            type:'POST',
            dataType:'json',
            success:function(data) {
                console.log(data['status']);
                if(data['status']==200){
                    $('#save_result_info').text('保存成功，3s后自动跳转到页面中...！');
                    showResultDiv(true);
                    window.setTimeout("showResultDiv(false);", 3000);
                    window.open('/accountApp/accountList/',target='_self')
                }else {
                    $('#save_result_info').text('保存失败，该身份证已经开通过账务账号！');
                    showResultDiv(true);
                    window.setTimeout("showResultDiv(false);", 3000);
                }

            }
        })
    }


}
function showResultDiv(flag) {
    var $divResult = $('#save_result_info');
    if (flag)
        $divResult.css({'display':'block'});
    else
        $divResult.css({'display':'none'});
}

//显示选填的信息项
function showOptionalInfo(imgObj) {
    var div = document.getElementById("optionalInfo");
    if (div.className == "hide") {
        div.className = "show";
        imgObj.src = "../../../static/images/hide.png";
    } else {
        div.className = "hide";
        imgObj.src = "../../../static/images/show.png";
    }
}

$(function () {
    checkPassword();
    checkName();
    ckeckidcard();
     login_name();
     checktelephone();
     recommender_id();
     email();
     zipcode();
     qq();
     $('#fee').click(function () {
        window.open('/tariffApp/feeList/',target='_self')
    });

    $('#service').click(function () {
        window.open('/serviceApp/serviceList/', target = '_self');
    });

});
//验证密码
function checkPassword() {
    $('#Password1').keyup(function () {
        var password = $(this).val();
        var reg = /^(?![^a-zA-Z]+$)(?!\D+$)(?![^_]+$).{0,30}$/;
        b = reg.test(password);
        if (b){
            $(this).next().next().css({'color':'black'});
        }else {
            $(this).next().next().css({'color':'red'});
        }
    });
    $('#Password2').keyup(function () {
        var comfirm_pwd = $(this).val();
        var pwd = $('#Password1').val();
          if (pwd == comfirm_pwd){
              $(this).next().next().css({'color':'black'})
          } else{
              $(this).next().next().css({'color':'red'})
            }
    })

}
//验证用户名
function checkName() {
     $('#name').keyup(function () {
        var name = $(this).val();
        var reg = /^[(a-zA-Z0-9\u4e00-\u9fa5)]{4,20}$/;
        b = reg.test(name);
        if (b){
            $(this).next().next().css({'color':'black'});
        }else {
            $(this).next().next().css({'color':'red'});
        }
    });
}
//验证电话
function checktelephone() {
    $('#telephone').keyup(function () {
        var telephone = $(this).val();
        var reg = /^[1]+[3,4,5,6,7,8,]+\d{9}$/;
        b = reg.test(telephone);
        if (b){
            $(this).next().next().css({'color':'black'});
        }else {
            $(this).next().next().css({'color':'red'});
        }
    });

}
//验证身份证号
function ckeckidcard() {
    $('#idcard').keyup(function () {
        var idcard = $(this).val();
        var reg =  /(^\d{15}$)|(^\d{18}$)/;
        b = reg.test(idcard);
        if (b){
            $(this).next().next().css({'color':'black'});
        }else {
            $(this).next().next().css({'color':'red'});
        }
    });
}
//验证账号
function login_name() {
        $('#login_name').keyup(function () {
        var login_name = $(this).val();
        var reg =  /^(?![^a-zA-Z]+$)(?!\D+$)(?![^_]+$).{0,30}$/;
        b = reg.test(login_name);
        if (b){
            $(this).next().next().css({'color':'black'});
        }else {
            $(this).next().next().css({'color':'red'});
        }
    });
}



function recommender_id(){
     $('#recommender_id').keyup(function () {
         var recommender_id = $(this).val();
         var reg =  /(^\d{18}$)/;
         b = reg.test(recommender_id);
         if (b){
             var year = recommender_id.substring(6,10);
             var month = recommender_id.substring(10,12);
             var day = recommender_id.substring(12,14);
             $(this).next().css({'color':'black'});
             $('#birthdate').val(year+'-'+month+'-'+day);
         }else {
             $(this).next().css({'color':'red'});
             $('#birthdate').val('');
         }
     });
}
function email() {
        $('#email').keyup(function () {
        var email = $(this).val();
        var reg =  /\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/;
        b = reg.test(email);
        if (b){
            $(this).next().css({'color':'black'});
        }else {
            $(this).next().css({'color':'red'});
        }
    });
}
function zipcode() {
     $('#zipcode').keyup(function () {
        var zipcode = $(this).val();
        var reg =  /^[1-9]{1}(\d{5})$/;
        b = reg.test(zipcode);
        if (b){
            $(this).next().css({'color':'black'});
        }else {
            $(this).next().css({'color':'red'});
        }
    });
}

function qq() {
         $('#qq').keyup(function () {
        var qq = $(this).val();
        var reg =  /^[1-9](\d{4,13})/;
        b = reg.test(qq);
        if (b){
            $(this).next().css({'color':'black'});
        }else {
            $(this).next().css({'color':'red'});
        }
    });
}


