// Sticky Header
$(window).scroll(function() {

    if ($(window).scrollTop() > 100) {
        $('.main_h').addClass('sticky');
    } else {
        $('.main_h').removeClass('sticky');
    }
});

// Mobile Navigation
$('.mobile-toggle').click(function() {
    if ($('.main_h').hasClass('open-nav')) {
        $('.main_h').removeClass('open-nav');
    } else {
        $('.main_h').addClass('open-nav');
    }
});

$('.main_h li a').click(function() {
    if ($('.main_h').hasClass('open-nav')) {
        $('.navigation').removeClass('open-nav');
        $('.main_h').removeClass('open-nav');
    }
});

// Navigation Scroll - ljepo radi materem
$('nav a').click(function(event) {
    var id = $(this).attr("href");
    var offset = 70;
    var target = $(id).offset().top - offset;
    $('html, body').animate({
        scrollTop: target
    }, 500);
    event.preventDefault();
});


// cover

$(window).load(function(){
    $('#cover').fadeOut(1000);
})




// scroll to anchor

$(document).ready(function() {
    $(".clickscroll").click(function(event) {
        console.log("clicked");
        var scroll = $(window).scrollTop();
        $('html, body').animate({
            scrollTop: ($(window).height() + scroll)
        }, 800);
    });
});


// image thing

var i = 0;
function nextPicture() {
    var pictures = document.getElementsByClassName("display-picture");

    var currentPic = pictures[i];
    i = (i + 1) % pictures.length;

    var nextPic = pictures[i];
    currentPic.classList.remove("current-picture");
    nextPic.classList.add("current-picture");
}

function prevPicture() {
    var pictures = document.getElementsByClassName("display-picture");

    var currentPic = pictures[i];
    i = (i > 0 ? ((i-1) % pictures.length) : pictures.length - 1);
    console.log(i);
    var prevPic = pictures[i];
    currentPic.classList.remove("current-picture");
    prevPic.classList.add("current-picture");
}