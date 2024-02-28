$(document).ready(function() {
    function fetchTranslation() {
        var languageCode = $('#language_code').val();

        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            $('#hello').text(data.hello);
        }).fail(function(error) {
            console.error('Error fetching translation:', error);
        });
    }

    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keydown(function(event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
