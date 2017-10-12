/*

 */

$(function () {
    $('#register-form').submit(function (e) {
        var $this = $(this);
        var $submit_btn = $this.find('button[type=submit]');
        var $password = $this.find('#password');
        var plain_pwd = $password.val();
        $password.val(md5(plain_pwd));
        var data = $this.serialize();

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
                    window.location.href = obj.msg.redirect_url;
                } else {
                    Materialize.toast(obj.msg.desc, 3000);
                    //$this.find('.card-panel').children('div:first-child').after()
                }
            },
            complete: function () {
                $submit_btn.removeClass('disabled');
                $password.val('');
            }
        });

    });
});