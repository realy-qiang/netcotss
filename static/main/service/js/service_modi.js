//保存成功的提示信息
function showResult(service_id) {
    $.getJSON(
        '/serviceApp/serviceModi/',
        {'service_id':service_id},
        function (data) {
            console.log(data)
        }
    )
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

function cancel() {
    window.location.href = '/serviceApp/serviceList/'
}

