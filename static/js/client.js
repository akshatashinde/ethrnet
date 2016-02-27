function isValidEmail(emailText) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailText);
};
function isValidName(emailText) {
    var pattern = new RegExp(/^[a-zA-Z]+$/i);
    return pattern.test(emailText);
};
function isValidNumber(emailText) {
    var pattern = new RegExp(/^[0-9]+$/i);
    return pattern.test(emailText);
};

$('input').blur(function(){
    $('input').attr('style', 'border:1px solid #d2d6de;');
    $("input[name*='q']").attr('style','');
    if ($(this)[0]==$('#id_name')[0] || $(this)[0]==$('#id_client_id')[0] || $(this)[0]==$('#id_email')[0] || $(this)[0]==$('#id_phone_number')[0] || $(this)[0]==$('#id_birth_date')[0])
    {
        var name = $('#id_name').val();
        var client_id = $('#id_client_id').val();
        var email = $('#id_email').val();
        var phone_number = $('#id_phone_number').val();
        var gender = $('#id_gender').val();
        var birth_date = $('#id_birth_date').val();
        phone_number_length = phone_number.length
        if( !isValidName(name) ) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Name!'});
            $('#id_name').attr('style', 'border:1px solid #dd4b39');
        }
        else if(client_id.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Client Id!'});
            $('#id_client_id').attr('style', 'border:1px solid #dd4b39;');
        }
        else if( !isValidEmail(email) ) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Email!'});
            $('#id_email').attr('style', 'border:1px solid #dd4b39;');
        }
        else if( !isValidNumber(phone_number) || 9 < phone_number_length <= 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Phone Number!'});
            $('#id_phone_number').attr('style', 'border:1px solid #dd4b39;');
        }
        else if(birth_date.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Birth Date!'});
            $('#id_birth_date').attr('style', 'border:1px solid #dd4b39;');
        }
        return true;
    }
    else if($(this)[0]==$('#id_flat_no')[0] || $(this)[0]==$('#id_society')[0] || $(this)[0]==$('#id_area')[0] || $(this)[0]==$('#id_city')[0] || $(this)[0]==$('#id_state')[0] || $(this)[0]==$('#id_country')[0] || $(this)[0]==$('#id_zipcode')[0]){
        var name = $('#id_flat_no').val();
        var society = $('#id_society').val();
        var area = $('#id_area').val();
        var city = $('#id_city').val();
        var state = $('#id_state').val();
        var country = $('#id_country').val();
        var zipcode = $('#id_zipcode').val();
        if(area.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Area!'});
            $('#id_area').attr('style', 'border:1px solid #dd4b39;');
        }
        else if(city.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid City!'});
            $('#id_city').attr('style', 'border:1px solid #dd4b39;');
        }
        else if(state.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid State!'});
            $('#id_state').attr('style', 'border:1px solid #dd4b39;');
        }
        else if(country.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Country!'});
            $('#id_country').attr('style', 'border:1px solid #dd4b39;');
        }
        else if(zipcode.length == 0) {
            $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Enter Valid Zipcode!'});
            $('#id_zipcode').attr('style', 'border:1px solid #dd4b39;');
        }

        return true;
    }

});
$('#collapseTwoClick').click(function(){
    var name = $('#id_name').val();
    var client_id = $('#id_client_id').val();
    var email = $('#id_email').val();
    var phone_number = $('#id_phone_number').val();
    var gender = $('#id_gender').val();
    var birth_date = $('#id_birth_date').val();
    if(!$('#collapseTwo').hasClass('in'))
    if (name.length == 0 || client_id.length == 0 || email.length == 0 || phone_number.length == 0 || phone_number.length > 10 || gender.length == 0 || birth_date.length == 0)
    {
        $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Provide valid Basic Information!'});
    }
    else{
        $('#basic_info').html('<img src="/static/img/gif-load.gif" height="20px" width="20px">Saving');
        //TODO AJAX FOR CLIENT
        create_client();
    }
});
$('li.dropdown.user.user-menu > a').click(function(){
    console.log('clicked')
    if($('li.dropdown.user.user-menu').hasClass('open')){
        $('li.dropdown.user.user-menu').removeClass('open');
    }
    else{
        $('li.dropdown.user.user-menu').addClass('open');
    }
});
$('#id_id_proof_types').blur(function(){
    var name = $('#id_flat_no').val();
    var society = $('#id_society').val();
    var area = $('#id_area').val();
    var city = $('#id_city').val();
    var state = $('#id_state').val();
    var country = $('#id_country').val();
    var zipcode = $('#id_zipcode').val();
    if (area.length == 0 || city.length == 0 || state.length == 0 || country.length == 0 || zipcode.length == 0)
    {
        $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Provide valid Address Information!'});
    }
    else{
        $('#advance_info').html('<img src="/static/img/gif-load.gif" height="20px" width="20px">Saving');
        //TODO AJAX FOR Address
        create_address();

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
            client_id: $('#id_client_id').val(),
            email : $('#id_email').val(),
            phone_number : '+91' + $('#id_phone_number').val(),
            gender : $('#id_gender').val(),
            birth_date : (($('#id_birth_date').val()).replace("-", "/")).replace("-", "/"),

         }, // data sent with the post request
        // handle a successful response
        success : function(response) {
            console.log(response)
            var response_dict = $.parseJSON(response)
            if(response_dict['success'] == true){
                delete response_dict['success']
                //TODO get client id and assign it to hidden field
                //TODO so that it can be used by other operations.
                $('#new_client_id').val(response_dict['client_id']);
                $.toaster({ priority : 'success', title : 'Client Success', message : 'Client successfully created.'});
                $('#basic_info').html('<b>Saved...</b>');
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


function create_address() {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url : "/client/address/new", // the endpoint
        type : "POST", // http method
        beforeSend: function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data : {
            flat_no : $('#id_flat_no').val(),
            society: $('#id_society').val(),
            area : $('#id_area').val(),
            city : $('#id_city').val(),
            state : $('#id_state').val(),
            country : $('#id_country').val(),
            zipcode : $('#id_zipcode').val(),

         }, // data sent with the post request
        // handle a successful response
        success : function(response) {
            console.log(response)
            var response_dict = $.parseJSON(response)
            if(response_dict['success'] == true){
                delete response_dict['success']
                //TODO get client id and assign it to hidden field
                //TODO so that it can be used by other operations.
                $('#new_address_id').val(response_dict['address_id']);
                $.toaster({ priority : 'success', title : 'Address Success', message : 'Address successfully created.'});
                $('#advance_info').html('<b>Saved...</b>');
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