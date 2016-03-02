
jq110(function () {
    'use strict';

    // Initialize the jQuery File Upload widget:
    jq110('#fileupload').fileupload({
        // Uncomment the following to send cross-domain cookies:
        //xhrFields: {withCredentials: true},
        //url: 'server/php/'
    });

    // Enable iframe cross-domain access via redirect option:
    jq110('#fileupload').fileupload(
        'option',
        'redirect',
        window.location.href.replace(
            /\/[^\/]*jq110/,
            '/cors/result.html?%s'
        )
    );

    if (window.location.hostname === 'blueimp.github.io') {
        // Demo settings:
        jq110('#fileupload').fileupload('option', {
            url: '//jquery-file-upload.appspot.com/',
            // Enable image resizing, except for Android and Opera,
            // which actually support image resizing, but fail to
            // send Blob objects via XHR requests:
            disableImageResize: /Android(?!.*Chrome)|Opera/
                .test(window.navigator.userAgent),
            maxFileSize: 5000000,
            acceptFileTypes: /(\.|\/)(gif|jpe?g|png)jq110/i
        });
        // Upload server status check for browsers with CORS support:
        if (jq110.support.cors) {
            jq110.ajax({
                url: '//jquery-file-upload.appspot.com/',
                type: 'HEAD'
            }).fail(function () {
                jq110('<div class="alert alert-danger"/>')
                    .text('Upload server currently unavailable - ' +
                            new Date())
                    .appendTo('#fileupload');
            });
        }
    } else {
        // Load existing files:
        jq110('#fileupload').addClass('fileupload-processing');
        var client_id = $('#new_client_id').val();
        jq110.ajax({
            // Uncomment the following to send cross-domain cookies:
            //xhrFields: {withCredentials: true},
            //url: jq110('#fileupload').fileupload('option', 'url'),
            url: '/upload/view/?client_id='+client_id,
            dataType: 'json',
            context: jq110('#fileupload')[0]
        }).always(function () {
            jq110(this).removeClass('fileupload-processing');
        }).done(function (result) {
            jq110(this).fileupload('option', 'done')
                .call(this, null, {result: result});
        });
    }
});