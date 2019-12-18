$(function () {
    $('#tologin').click(function () {
        var super_number = $('input[name=super_number]').val();
        var password = $('input[name=password]').val();
        var imgCode = $('input[name=imgCode]').val();
        $.post('/adm/checklogin/',
            {'super_number':super_number,
              'password':password,
                'imgCode':imgCode,
            },
            function (data) {
                if(data['status']==200){
                    window.location.href = '/adm/home/'
                }else {
                    $('#hint').html(data['msg'])

                }
            }
            )
    })
});

function chageImage() {
    var i = document.getElementById("changeImage");
    //获取img标签的dom对象,可以使用src方法发起请求
    i.src = '/adm/get_code/?'+Math.random();
}