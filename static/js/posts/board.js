/*

 */

$(function () {
    $('#new-post-form').submit(function (e) {
        var $this = $(this);
        var $newPostTitle = $('#new-post-title');
        var $newPostContent = $('#new-post-content');
        var input_is_empty = false;
        $.each([$newPostTitle, $newPostContent], function (i, $item) {
            if (!$item.val()) {
                $item.focus();
                input_is_empty = true;
                return false;
            }
        });
        if (input_is_empty) return false;
        e.preventDefault();
        addLoadingCover();
        $.ajax({
            url: $this.attr('action'),
            type: $this.attr('method'),
            data: {
                'title': $newPostTitle.val(),
                'content': $newPostContent.val()
            },
            success: function (callback) {
                var obj = $.parseJSON(callback);
                console.log(obj);
                if (obj.result) {
                    window.location.reload();
                } else {
                    var msg = translate_exception(obj.msg.code);
                    Materialize.toast(msg || obj.msg.desc, 3000);
                }
            },
            complete: function () {
                removeLoadingCover();
            }
        });

    });
});