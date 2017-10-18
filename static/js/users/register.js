/*

 */

$(function () {
    $('#register-form').submit(function (e) {

        var $this = $(this);
        var $submit_btn = $this.find('button[type=submit]');
        var $username = $this.find('#username');
        var $password = $this.find('#password');
        var $email = $this.find('#email');
        var plain_pwd = $password.val();
        if (!$username.val()) {
            $username.focus();
            return false;
        } else if (!plain_pwd) {
            $password.focus();
            return false;
        } else if (!$email.val()) {
            $email.focus();
            return false;
        }
        $password.val(md5(plain_pwd));
        var data = $this.serialize();

        // prevent default submit action
        e.preventDefault();

        $submit_btn.addClass('disabled');
        addLoadingCover();
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
                    var msg = translate_exception(obj.msg.code);
                    Materialize.toast(msg, 3000);
                }
            },
            complete: function () {
                $submit_btn.removeClass('disabled');
                $password.val('').focus();
                removeLoadingCover();
            }
        });

    });
});