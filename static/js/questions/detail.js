/**
 * Created by Oliver on 2017/10/25 0025.
 */

// scroll spy
$(document).ready(function(){
    $('.scrollspy').scrollSpy();
  });

// submit answer
$(function () {
    $('#new-answer-form').submit(function (e) {
        var $this = $(this);
        var $newAnswerContent = $('#new-answer-content');

        if (!$newAnswerContent.val()) {
            $newAnswerContent.focus();
            return false;
        }
        console.log($newAnswerContent.val());
        e.preventDefault();
        addLoadingCover();
        $.ajax({
            url: $this.attr('action'),
            type: $this.attr('method'),
            data: {
                'content': $newAnswerContent.val()
            },
            success: function (callback) {
                var obj = $.parseJSONAndTrans(callback);
                console.log(obj);
                if (obj.result) {
                    window.location.reload();
                } else {
                    Materialize.toast(obj.msg.desc, 3000);
                }
            },
            complete: function () {
                removeLoadingCover();
            }
        });

    });
});