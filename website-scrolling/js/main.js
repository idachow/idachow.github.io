$(document).ready(function() {
    $(".clickscroll").click(function(event) {
        console.log("clicked");
        var scroll = $(window).scrollTop();
        $('html, body').animate({
            scrollTop: ($(this).height() + scroll)
        }, 800);
    });
});
