
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

    if (error != ""){
        $.toaster({ priority : 'danger', title : 'Plan Failed', message : error});
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
            FUP_limit : $('#id_FUP_limit').val(),
            post_FUP_speed : $('#id_post_FUP_speed').val(),
            installation_charges : $('#id_installation_charges').val(),
            subscription_amount : $('#id_subscription_amount').val()
         }, // data sent with the post request
        // handle a successful response
        success : function(response) {
            var response_dict = $.parseJSON(response)
            if(response_dict['success'] == true){
                delete response_dict['success']
                var tds = '<tr>';
                tds += '<td>' + response_dict['id'] + '</td>';
                tds += '<td>' + response_dict['plan_type'] + '</td>';
                tds += '<td>' + response_dict['price'] + '</td>';
                if (response_dict['is_active'] == true){
                    tds += '<td><span class="label label-primary">Acitve</span></td>';
                }else{
                    tds += '<td><span class="label label-danger">Deactive</span></td>';
                }
                tds += '<td>' + response_dict['FUP_limit'] + '</td>';
                tds += '<td>' + response_dict['download_speed'] + '</td>';
                tds += '<td>' + response_dict['installation_charges'] + '</td>';
                tds += '<td>' + response_dict['subscription_amount'] + '</td>';
                tds += '<td><button class="btn btn-default btn-sm"><i class="fa fa-trash-o"></i></button>&nbsp;<button class="btn btn-default btn-sm"><i class="fa fa-edit"></i></button></td>'
                tds += '</tr>';
                $("tbody > tr:nth-child(1)").after(tds);
                $('#plan_type').val("");
                $('#id_price').val("");
                $('#id_duration').val("");
                $('#id_FUP_limit').val("");
                $('#id_download_speed').val("");
                $('#id_post_FUP_speed').val("");
                $('#id_installation_charges').val("");
                $('#id_subscription_amount').val("");
                $.toaster({ priority : 'success', title : 'Plan Success', message : 'Plan successfully created.'});

            }
            else{
                $.toaster({ priority : 'danger', title : 'Plan Failed', message : 'Plan not created.'});
            }
        },
        error: function(response) {
                $.toaster({ priority : 'danger', title : 'Plan Failed', message : 'Plan not created.'});
            },
        // handle a non-successful response
    });
};



$("#submitclient").click(function()
{
    var error = ""
    var name = $('#id_name').val();
    var email = $('#id_email').val();
    var client_id = $('#id_client_id').val();
    var phone_number = $('#id_phone_number').val();
    var address = $('#id_address').val();
    var flat_no = $('#id_flat_no').val();
    var society = $('#id_society').val();
    var area = $('#id_area').val();
    var city = $('#id_city').val();
    var state = $('#id_state').val();
    var country = $('#id_country').val();
    var zipcode = $('#id_zipcode').val();
    if(name == ""){
        error = "Name not Provided";
    }
    else if(email == ""){
        error = "Email not Provided";
    }
    else if(client_id == ""){
        error = "Email not Provided";
    }
    else if(phone_number == ""){
        error = "Phone Number not Provided";
    }
    else if(address == ""){
        error = "Address not Provided";
    }
    else if(flat_no == ""){
        error = "Address not Provided";
    }
    else if(society == ""){
        error = "Address not Provided";
    }
    else if(area == ""){
        error = "Address not Provided";
    }
    else if(city == ""){
        error = "City not Provided";
    }
    else if(state == ""){
        error = "State not Provided";
    }
    else if(country == ""){
        error = "Country not Provided";
    }
    else if(zipcode == ""){
        error = "Zipcode not Provided";
    }

    if (error != ""){
        $.toaster({ priority : 'danger', title : 'Client Failed', message : error});
        error = "";
    }
    else{
            create_client();
    }
});


function create_client() {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url : "/client/new", // the endpoint
        type : "POST", // http method
        beforeSend: function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data : {
            name : $('#id_name').val(),
            email : $('#id_email').val(),
            client_id : $('#id_client_id').val(),
            phone_number : $('#id_phone_number').val(),
            address : $('#id_address').val(),
            flat_no : $('#id_flat_no').val(),
            society : $('#id_society').val(),
            area : $('#id_area').val(),
            city : $('#id_city').val(),
            state : $('#id_state').val(),
            country : $('#id_country').val(),
            zipcode : $('#id_zipcode').val()
         }, // data sent with the post request
        // handle a successful response
        success : function(response) {
            var response_dict = $.parseJSON(response)
            if(response_dict['success'] == true){
                delete response_dict['success']
                var tds = '<tr>';
                tds += '<td>' + response_dict['client_id'] + '</td>';
                tds += '<td>' + response_dict['name'] + '</td>';
                tds += '<td>' + response_dict['email'] + '</td>';
                tds += '<td>' + response_dict['phone_number'] + '</td>';
                tds += '<td><button class="btn btn-default btn-sm"><i class="fa fa-trash-o"></i></button>&nbsp;<button class="btn btn-default btn-sm"><i class="fa fa-edit"></i></button></td>'
                tds += '</tr>';
                $("tbody > tr:nth-child(1)").after(tds);
                $('#id_name').val("");
                $('#id_email').val("");
                $('#id_phone_number').val("");
                $('#id_address').val("");
                $('#id_flat_no').val("");
                $('#id_society').val("");
                $('#id_area').val("");
                $('#id_city').val("");
                $('#id_state').val("");
                $('#id_country').val("");
                $('#id_zipcode').val("");
                $.toaster({ priority : 'success', title : 'Client Success', message : 'Client successfully created.'});
            }
            else{
                $.toaster({ priority : 'danger', title : 'Client Failed', message : 'Client not created.'});
            }
        },
        error: function(response) {

                $.toaster({ priority : 'danger', title : 'Client Failed', message : 'Client not created.'});
            },
        // handle a non-successful response
    });
};