
// 排序按钮的点击事件
// function sort(btnObj, page, value) {
//     if (value == '时长') {
//         if (btnObj.className == "sort_desc") {
//             btnObj.className = "sort_asc";
//
//             window.location.href = "/tariffApp/feeList/" + "?page=" + page + "&orderBy=sort_asc"+"&order=time"
//         } else {
//             btnObj.className = "sort_desc";
//             window.location.href = "/tariffApp/feeList/" + "?page=" + page + "&orderBy=sort_desc"+"&order=time"
//         }
//     } else {
//         if (value == '基费') {
//             if (btnObj.className == "sort_desc") {
//                 btnObj.className = "sort_asc";
//
//                 window.location.href = "/tariffApp/feeList/" + "?page=" + page + "&orderBy=sort_asc"+"&order=BaseCost"
//             } else {
//                 btnObj.className = "sort_desc";
//                 window.location.href = "/tariffApp/feeList/" + "?page=" + page + "&orderBy=sort_desc"+"&order=BaseCost"
//             }
//         } else {
//             if (btnObj.className == "sort_desc") {
//                 btnObj.className = "sort_asc";
//
//                 window.location.href = "/tariffApp/feeList/" + "?page=" + page + "&orderBy=sort_asc"+"&order=UnitCost"
//             } else {
//                 btnObj.className = "sort_desc";
//                 window.location.href = "/tariffApp/feeList/" + "?page=" + page + "&orderBy=sort_desc"+"&order=UnitCost"
//
//             }
//         }
//     }
//
//
// }


$(function () {
    $('#unit_cost_sort').click(function () {
        $(this).toggleClass('sort_asc sort_desc')
        var sort_type = $(this).attr('class')
        window.location.href = '/tariffApp/orderUnitCost/?orderBy='+sort_type
    })

    $('#cost_sort').click(function () {
        $(this).toggleClass('sort_asc sort_desc')
        var sort_type = $(this).attr('class')
        window.location.href = '/tariffApp/orderByCost/?orderBy='+sort_type
    })

    $('#time_sort').click(function () {
        $(this).toggleClass('sort_asc sort_desc');
        var sort_type = $(this).attr('class')
        window.location.href = '/tariffApp/orderByTime/?orderBy='+sort_type
    })
})

//启用
function startFee(id) {
    var r = window.confirm("确定要启用此资费吗？资费启用后将不能修改和删除。");

    alert(id)

    if (r) {
        document.getElementById("operate_result_info").style.display = "block";
        window.location.href = "/tariffApp/startUp/" + "?id=" + id;

    }

}

//删除
function deleteFee(id) {
    var r = window.confirm("确定要删除此资费吗？");
    if (r) {
        document.getElementById("delete_result_info").style.display = 'block';
        window.location.href = "/tariffApp/deleteFee" + "?id=" + id;
    }

}