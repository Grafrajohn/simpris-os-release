/**
 * Created by Graham on 24/09/2015.
 */

"use strict";

simpris.common.do_something = function () {

    //$('#spnError').empty();
}

simpris.common.getRandomColour = function () {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
};

simpris.common.raiseError = function (module, submodule, action, subaction, errMessage, token) {
    var err_data = {
        csrfmiddlewaretoken: token,
        module: module,
        submodule: submodule,
        action: action,
        subaction: subaction,
        description: errMessage
    }
    $.ajax({
        url: '/api/error/insert/',
        data: err_data,
        type: 'POST'
    })
    .error(function(err){
    })
    .success(function(response){
    });
};

simpris.common.errorNotify = function (errMessage) {
    $('#div-notification').append(errMessage);
    $('#div-notification').removeClass('alert-success');
    $('#div-notification').addClass("alert-danger");
    $("#div-notification").css('display','block');
}

simpris.common.successNotify = function (statusMessage) {
    $('#div-notification').append(statusMessage);
    $('#div-notification').removeClass('alert-danger');
    $('#div-notification').addClass("alert-success");
    $("#div-notification").css('display','block');
}