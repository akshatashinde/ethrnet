function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var row = $('.dynamic-form:first').clone(true).get(0);
    $(row).removeAttr('id').insertAfter($('.dynamic-form:last')).children('.hidden').removeClass('hidden');
    $(row).children().not(':last').children().each(function() {
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
    });
    $(row).find('.delete-row').click(function() {
        deleteForm(this, prefix);
    });
    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
    if ( $('tbody > tr').length > 3 ){
        $('tbody > tr > td:nth-child(6)').show();
    }
    count = -1;
$("#invoice_table_body tr").each(function(){
    if (count + 2 == $("tbody tr").length){
        return false;
    }
  $( this ).find( "td" ).first().html( count + 1 );
  count = count + 1
});


    return false;
}

function deleteForm(btn, prefix) {
    $(btn).parents('.dynamic-form').remove();
    var forms = $('.dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i=0, formCount=forms.length; i<formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function() {
            updateElementIndex(this, prefix, i);
        });
    }
    if ( $('tbody > tr').length == 3 ){
        $('tbody > tr > td:nth-child(6)').hide();
    }
    count = -1;
$("#invoice_table_body tr").each(function(){
    if (count + 2 == $("tbody tr").length){
        return false;
    }
  $( this ).find( "td" ).first().html( count + 1 );
  count = count + 1
});


    return false;
}
$('#submitinvoice').click(function() {
});
count = -1;
$("#invoice_table_body tr").each(function(){
    if (count + 2 == $("tbody tr").length){
        return false;
    }
  $( this ).find( "td" ).first().html( count + 1 );
  count = count + 1
});
$(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });