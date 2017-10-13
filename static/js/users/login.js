/*
For users' login
 */

$(function () {
    $('#login-form').submit(function (e) {
        // prevent default submit action
        e.preventDefault();
        var from_url = $.getUrlParam('from');
        var $this = $(this);
        var $submit_btn = $this.find('button[type=submit]');
        var $password = $this.find('#password');
        var $usernameOrEmail = $this.find('#username-or-email');
        console.log($usernameOrEmail);
        if (!$usernameOrEmail.val()) {
            showTooltip({
                target: $usernameOrEmail,
                tooltip: '用户名/邮箱不能为空'
            })
        }
        var plain_pwd = $password.val();
        $password.val(md5(plain_pwd));
        var data = $this.serialize();


        return false;
        $.ajax({
            url: $this.attr('action'),
            data: data,
            type: 'POST',
            success: function (callback) {
                var obj = $.parseJSON(callback);
                if (obj.result) {
                    if (from_url) {
                        window.location.href = href;
                    } else {
                        window.location.href = '/';
                    }

                } else {
                    Materialize.toast(obj.msg.desc, 3000);
                }
            },
            complete: function () {
                $submit_btn.removeClass('disabled');
                $password.val('');
            }
        });

    });
});