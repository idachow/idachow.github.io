$(function(){
  $("#navbar").load("navigation.html"); 
});

$(function(){
  $("#foot").load("footer.html"); 
});

/****gettingstarted****/

$(function(){
    $navarrow = ("<span></span>");

	$.hideAll = function () {
		$("#initialtext").hide();
		$("#interactivity").hide();
		$("#electronics").hide();
		$("#programming").hide();
        $("button").attr("class", "btn");
	};

	$("#interactivity").hide();
	$("#electronics").hide();
	$("#programming").hide();



	$( "#buttoninteractivity" ).click(function() {
			$.hideAll();
	        $( "#interactivity" ).fadeToggle("slow", "linear");
            $(this).attr("class", "btn btn-warning");
	});



	$( "#buttonelectronics" ).click(function() {
			$.hideAll();
	        $( "#electronics" ).fadeToggle("slow");
            $(this).attr("class", "btn btn-warning");
	});

	$( "#buttonprogramming" ).click(function() {
			$.hideAll();
	        $( "#programming" ).fadeToggle("slow");
            $(this).attr("class", "btn btn-warning");
	});
});

/****gallery lightbox***/

$(function(){

	var $overlay = $('<div id="overlay"></div>');
    var $image = $("<img>");
    var $caption = $("<p></p>");

     /**text attached to image attached to overlay attached to body*/
    $overlay.append($image);
    $overlay.append($caption);
	$("body").append($overlay);

	$("#folioGallery a").click(function(event){
		event.preventDefault();
		var imgLoc = $(this).children("img").attr("src");
        $image.attr("src",imgLoc);
		$overlay.show();

        var captionText = $(this).children("img").attr("alt");
        $caption.text(captionText);

        /*need a link out to original source!*/
	});

    /*remove overlay w click*/
    $overlay.click(function(){
        $overlay.hide();
    });

});


//***mobile nav****//

$(document).ready(function(){

    $(window).scroll(function(){
        var window_top = $(window).scrollTop() + 10; // 
        var div_top = $('#subnav').offset().top;
            if (window_top > div_top) {
                $('nav').addClass('stick');
            } else {
                $('nav').removeClass('stick');
            }
    });

});

