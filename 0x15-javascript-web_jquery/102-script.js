$(document).ready(function () {
    function translate() {
        var languageCode = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
            $('#hello').text(data.hello);
        }).fail(function (error) {
            console.error('Error fetching translation:', error);
        });
    }

    $('#btn_translate').click(translate);

    $('#language_code').focus(function () {
        $(this).keydown(function (event) {
            if (event.keyCode === 13) {
                translate();
            }
        });
    });
});
