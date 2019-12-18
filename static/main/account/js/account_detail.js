$(function () {

    $('#fee').click(function () {
        window.open('/tariffApp/feeList/', target = '_self');
    });

    $('#service').click(function () {
        window.open('/serviceApp/serviceList/', target = '_self');
    });
});