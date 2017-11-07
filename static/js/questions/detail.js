/**
 * Created by Oliver on 2017/10/25 0025.
 */

function getAnswerId(section) {
    var $section = getJQueryObject(section);
    return $section.attr('id').replace('answer-', '')
}

// bind submit comment
function bindSubmitComment(section) {
    var $section = getJQueryObject(section);
    var $form = $section.find('.new-comment-form');
    // submit new comment
    $form.submit(function (e) {
        var $this = $(this);
        var $newComment = $this.find('textarea');
        if (!$newComment.val()) {
            $newComment.focus();
            return false;
        }
        console.log($newComment.val());
        e.preventDefault();
        addLoadingCover();
        $.ajax({
            url: $this.attr('action'),
            type: $this.attr('method'),
            data: {
                'content': $newComment.val(),
                'aid': getAnswerId($section)
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
}


// scroll spy
$(document).ready(function(){
    $('.scrollspy').scrollSpy();
  });

$(function () {
    // submit answer
    $('#new-answer-form').submit(function (e) {
        var $this = $(this);
        var $newAnswer = $('#new-answer-content');

        if (!$newAnswer.val()) {
            $newAnswer.focus();
            return false;
        }
        e.preventDefault();
        addLoadingCover();
        $.ajax({
            url: $this.attr('action'),
            type: $this.attr('method'),
            data: {
                'content': $newAnswer.val()
            },
            success: function (callback) {
                var obj = $.parseJSON(callback);
                if (obj.result) {
                    window.location.reload();
                } else {
                    console.log(obj.message);
                    var msg = translateException(obj.message);
                    Materialize.toast(msg, 3000);
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
        var answerId = getAnswerId($section);
        var baseUrl = getRelativeUrl();
        var textArea = '<div class="row new-comment-wrapper">\n' +
            '  <form class="col s12 new-comment-form" method="post" action="' + baseUrl + 'new_comment/">\n' +
            document.getElementById('csrf-token').outerHTML +
            '    <div class="row">\n' +
            '      <div class="input-field col s12">\n' +
            '        <textarea id="new-comment-' + answerId + '" class="materialize-textarea" minlength="2"></textarea>\n' +
            '        <label for="new-comment-' + answerId + '" class="">我的看法</label>\n' +
            '      </div>\n' +
            '    </div>\n' +
            '    <button class="btn waves-effect waves-light" type="submit" name="action">评论</button>\n' +
            '  </form>\n' +
            '</div>';

        var $newCommentWrapper = $section.find('.new-comment-wrapper');

        if ($this.hasClass('rotate-0')) {
            $this.removeClass('rotate-0').addClass('rotate-90');
        } else if ($this.hasClass('rotate-90')) {
            $this.removeClass('rotate-90').addClass('rotate-0');
        } else {
            $this.addClass('rotate-90');
        }
        if ($newCommentWrapper.length > 0) {
            $newCommentWrapper.slideToggle();
        } else {
            $(textArea).hide().appendTo($section).slideDown();
            bindSubmitComment($section);
        }
    });
    
    // show more comments
    $('.show-more-comments').click(function (e) {
        var $this = $(this);
        $this.parent().parent().find('li.hide').hide().removeClass('hide').fadeIn('slow');
        $this.remove();
    });


});