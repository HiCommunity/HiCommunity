/*
For users' login
 */

$(function () {
    $('#login-form').submit(function (e) {
        // prevent default submit action
        e.preventDefault();
        var next_url = $.getUrlParam('next');
        var $this = $(this);
        var $submit_btn = $this.find('button[type=submit]');
        var $password = $this.find('#password');
        var $usernameOrEmail = $this.find('#username-or-email');
        if (!$usernameOrEmail.val()) {
            $usernameOrEmail.focus();
            return false;
        } else if (!$password.val()) {
            $password.focus();
            return false;
        }
        var hashed_password = md5($password.val());
        $password.val(hashed_password);
        var checked = $('#remember-me').is(':checked');
        var data = {
            'username_or_email': $usernameOrEmail.val(),
            'password': hashed_password,
            'checked': checked
        };
        $submit_btn.addClass('disabled');
        addLoadingCover();
        $.ajax({
            url: $this.attr('action'),
            data: data,
            type: $this.attr('method'),
            success: function (callback) {
                var obj = $.parseJSON(callback);
                if (obj.result) {
                    if (next_url) {
                        window.location.href = next_url;
                    } else {
                        window.location.href = '/';
                    }
                } else {
                    var msg = translateException(obj.message)
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