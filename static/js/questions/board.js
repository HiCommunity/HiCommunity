/*

 */

$(function () {
    $('#new-question-form').submit(function (e) {
        var $this = $(this);
        var $newQuestionTitle = $('#new-question-title');
        var $newQuestionContent = $('#new-question-content');
        var input_is_empty = false;
        $.each([$newQuestionTitle, $newQuestionContent], function (i, $item) {
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
                'title': $newQuestionTitle.val(),
                'content': $newQuestionContent.val()
            },
            success: function (callback) {
                var obj = $.parseJSON(callback);
                console.log(obj);
                if (obj.result) {
                    window.location.reload();
                } else {
                    var msg = translateException(obj.message);
                    Materialize.toast(msg, 3000);
                }
            },
            complete: function () {
                removeLoadingCover();
            }
        });

    });
});