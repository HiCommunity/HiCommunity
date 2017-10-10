/*

 */

$(function () {
    $('#register-form').submit(function (e) {
        var $this = $(this);
        var $submit_btn = $this.find('button[type=submit]');
        var data = $this.serialize();
        var $password = $this.find('#password');
        var plain_pwd = $password.val();
        $password.val(md5(plain_pwd));

        // prevent default submit action
        e.preventDefault();

        $submit_btn.addClass('disabled');
        $.ajax({
            url: $this.attr('action'),
            data: data,
            type: 'POST',
            success: function (callback) {
                var obj = $.parseJSON(callback);
                console.log(obj);
                if (obj.result) {

                } else {

                }
            },
            complete: function () {
                $submit_btn.removeClass('disabled');
                $password.val('');
            }
        });

    });
});