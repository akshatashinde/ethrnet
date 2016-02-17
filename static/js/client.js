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

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
};

$('input').blur(function(){
    $('input').attr('style', 'border:1px solid #d2d6de;');
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
});
$('#collapseTwoClick').click(function(){
    var name = $('#id_name').val();
    var client_id = $('#id_client_id').val();
    var email = $('#id_email').val();
    var phone_number = $('#id_phone_number').val();
    var gender = $('#id_gender').val();
    var birth_date = $('#id_birth_date').val();
    if(!$('#collapseTwo').hasClass('in'))
    if (name.length == 0 || client_id.length == 0 || email.length == 0 || phone_number.length == 0 || gender.length == 0 || birth_date.length == 0)
    {
        $.toaster({ priority : 'danger', title : 'Validation Error!', message : 'Provide valid Basic Information!'});
    }
    else{
        $('#basic_info').html('<img src="/static/img/gif-load.gif" height="20px" width="20px">Saving');
    }
});