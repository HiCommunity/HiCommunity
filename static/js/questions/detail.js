/**
 * Created by Oliver on 2017/10/25 0025.
 */

// bind submit comment
function bindSubmitComment(form) {
    var $form = getJQueryObject(form);
    $form.submit(function (e) {
        var $this = $(this);
        var $textArea = $this.find('textarea');
        if (!$textArea.val()) {
            $textArea.focus();
            return false;
        }
        e.preventDefault();
    });
}


// scroll spy
$(document).ready(function(){
    $('.scrollspy').scrollSpy();
  });

$(function () {
    // submit answer
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

    // show comment dialog
    $('.show-comment').click(function (e) {
        var $this = $(this);
        var $section = $this.parent().parent();
        var answerId = $section.attr('id');

        var textArea = '<div class="row comment-wrapper">\n' +
            '  <form class="col s12 comment-form">\n' +
            '    <div class="row">\n' +
            '      <div class="input-field col s12">\n' +
            '        <textarea id="textarea-' + answerId + '" class="materialize-textarea" minlength="10"></textarea>\n' +
            '        <label for="textarea-' + answerId + '" class="">我的看法</label>\n' +
            '      </div>\n' +
            '    </div>\n' +
            '    <button class="btn waves-effect waves-light" type="submit" name="action">评论</button>\n' +
            '  </form>\n' +
            '</div>';

        var $commentWrapper = $section.find('.comment-wrapper');

        if ($this.hasClass('rotate-0')) {
            $this.removeClass('rotate-0').addClass('rotate-90');
        } else if ($this.hasClass('rotate-90')) {
            $this.removeClass('rotate-90').addClass('rotate-0');
        } else {
            $this.addClass('rotate-90');
        }
        if ($commentWrapper.length > 0) {
            $commentWrapper.slideToggle();
        } else {
            $(textArea).hide().appendTo($section).slideDown();
        }
    });


});