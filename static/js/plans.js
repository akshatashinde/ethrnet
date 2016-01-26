
$("#submitplans").click(function()
{
    var error = ""
    var plan_type = $('#plan_type').val();
    var price = $('#id_price').val();
    var duration = $('#id_duration').val();
    var download_speed = $('#id_download_speed').val();
    var post_FUP_speed = $('#id_post_FUP_speed').val();
    var installation_charges = $('#id_installation_charges').val();
    var subscription_amount = $('#id_subscription_amount').val();
    if(plan_type == ""){
        error = "Plan not selected";
    }
    else if(price == ""){
        error = "Price not selected";
    }
    else if(duration == ""){
        error = "Duration not selected";
    }
    else if(download_speed == ""){
        error = "Download speed not selected";
    }
    else if(post_FUP_speed == ""){
        error = "Post FUP speed not selected";
    }
    else if(installation_charges == ""){
        error = "Installation charges not selected";
    }
    else if(subscription_amount == ""){
        error = "Subscription amount not selected";
    }

    if (error != ""){
        $('#plan_error').text(error);
        $("#plan_error").fadeToggle(100);
        $("#plan_error").fadeOut(3000);
        error = "";
    }
    else{
            get_notifications();
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function get_notifications() {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url : "/plan/new", // the endpoint
        type : "POST", // http method
        beforeSend: function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data : {
            plan_type : $('#plan_type').val(),
            price : $('#id_price').val(),
            duration : $('#id_duration').val(),
            download_speed : $('#id_download_speed').val(),
            post_FUP_speed : $('#id_post_FUP_speed').val(),
            installation_charges : $('#id_installation_charges').val(),
            subscription_amount : $('#id_subscription_amount').val()
         }, // data sent with the post request
        // handle a successful response
        success : function(response) {
            if(response == 'Success'){
                $('#plan_success').text("Plan added Successfully");
                $("#plan_success").fadeToggle(100);
                $("#plan_success").fadeOut(3000);
                $('#plan_type').val("");
                $('#id_price').val("");
                $('#id_duration').val("");
                $('#id_download_speed').val("");
                $('#id_post_FUP_speed').val("");
                $('#id_installation_charges').val("");
                $('#id_subscription_amount').val("");
            }
            else{
                $('#plan_error').text("Provide valid inputs.");
                $("#plan_error").fadeToggle(100);
                $("#plan_error").fadeOut(3000);
            }
        },
        error: function(response) {
                $('#resultdisplay').html("");
            },
        // handle a non-successful response
    });
};