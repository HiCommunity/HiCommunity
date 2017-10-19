/*

 */

$(function () {
    $('#new-post-form').submit(function (e) {
        // prevent default submit action
        e.preventDefault();
        var $newPostTitle = $('#new-post-title');
        var $newPostContent = $('#new-post-content');
        var $newPostSubmitBtn = $('#new-post-submit-btn');
        $.each([$newPostTitle, $newPostContent], function (i, item) {
            console.log(i);
            console.log(item);
        })

    });
});