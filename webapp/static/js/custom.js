$(document).ready(function() {
    $("form[name='user-form']").validate({
        rules: {
            name: "required",
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            name: "Please enter your Name",
            email: {
                required: "Please enter your email address",
                email: "Please enter a valid email address"
            }
        },
        submitHandler: function(form) {
            waitingDialog.show("Sending...");
            $.ajax({
                type: 'POST',
                url: $("#user-form").attr("action"),
                data: $("#user-form").serialize(),
                success: function (response) {
                    waitingDialog.hide();
                    var message = "";
                    var btnType = "";
                    if(parseInt(response.status) === 1){
                        btnType = "btn-success";
                        message = prepMessage(response.message, "#009900", "fa-check", "Success");
                    }else{
                        btnType = "btn-danger";
                        var errors = ''; var i;
                        for (i in response.message) {
                            errors +=  response.message[i] + '<br />';
                        }
                        message = prepMessage(errors, "#d9534f", "fa-exclamation-triangle", "Error");
                    }
                    bootbox.alert(message, function () {
                        $("#user-form")[0].reset();
                    }).find(".modal-footer .btn-primary").removeClass("btn-primary").addClass(btnType);
                }
            });
        }
    });

    var prepMessage = function (message, color, fontIcon, heading) {
        return "<h3 class='text-center' style='color: " + color + ";'><span class='fa " + fontIcon + "'></span>&nbsp;" + heading + " </h3><hr><p class='text-center' style='color: " + color + ";'>" + message + "</p>";
    };
});