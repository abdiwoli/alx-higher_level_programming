#!/usr/bin/node
#!/usr/bin/node
$(document).ready(function() {
    $('#add_item').click(function() {
        $('UL.my_list').append('<li>Item</li>');
    });
    $('#clear_list').click(function() {
        $('UL.my_list').empty();
    });
    $('#remove_item').click(function() {
        $('UL.my_list li:last').remove();
    });
});
