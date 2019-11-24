$(document).ready(function () {
    var replaceBtn = $('#replaceKeyBtn');
    var replaceBtnSpinner = $('#replaceBtnSpinner');

    replaceBtn.on('click', function () {
        var key = $('#key').val();
        replaceBtnSpinner.prop("hidden", false);
        replaceBtn.prop("disabled", true);

        replaceKey(key);
    });
});

function replaceKey(key) {
    var resultText = $('#result_text_replace');
    var resultAddress = $('#result_address_replace');
    var resultLink = $('#result_link_replace');
    $.ajax({
        method: 'POST',
        url: "/replace/",
        data: {
            'key': key
        },
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function (response) {
            var data = JSON.parse(response);
            if (data['status'] == 0) { //show error
                resultText.html('<b>' + data['message'] + '</b>');
            } else {
                resultText.html('Country: <code><b>' + data['country'] + '</b></code>');
                resultLink.html('Invite link: <code><a href="' + data['Link'] + '" target="_blank">' + data['Link'] + '</a></code>');
                resultAddress.html('Address: <code><b>' + data['Adress'] + "</b></code>");
            }

            $('#replaceBtnSpinner').prop("hidden", true);
        }
    });
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}