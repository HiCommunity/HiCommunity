/*
For users' login
 */

$(function () {
    $('#login-form').submit(function (e) {
        e.preventDefault();
        var next_url = $.getUrlParam('next');
        var $this = $(this);
        var $submit_btn = $this.find('button[type=submit]');
        var $password = $this.find('#password');
        var origin_password = $password.val();
        var $usernameOrEmail = $this.find('#email');
        if (!$usernameOrEmail.val()) {
            $usernameOrEmail.focus();
            return false;
        } else if (!origin_password) {
            $password.focus();
            return false;
        }
        var hashed_password = md5(origin_password);
        $password.val(hashed_password);
        var checked = $('#keep-login').is(':checked');
        var data = {
            'email': $usernameOrEmail.val(),
            'password': hashed_password,
            'keep_login': checked,
            'password_length': origin_password.length
        };
        $submit_btn.addClass('disabled');
        addLoadingCover();

        $.ajax({
            url: $this.attr('action'),
            data: data,
            type: $this.attr('method'),
            success: function (callback) {
                var obj = $.parseJSON(callback);
                console.log(obj);
                if (obj.result) {
                    if (next_url) {
                        window.location.href = next_url;
                    } else {
                        window.location.href = '/';
                    }
                } else {
                    var msg = translateException(obj.message);
                    Materialize.toast(msg, 3000);
                }
            },
            complete: function () {
                $password.val('').focus();
                $submit_btn.removeClass('disabled');
                removeLoadingCover();
            }
        });

    });
});