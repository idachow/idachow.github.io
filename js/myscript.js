$(function(){
  $("#navbar").load("navigation.html"); 
});

$(function(){
  $("#foot").load("footer.html"); 
});

/****gettingstarted****/

$(function(){
	$("#interactivity").hide();
	$("#electronics").hide();
	$("#programming").hide();
	$("#links").hide();
	$("#projects").hide();
	$("#inspa").hide();
});

$(function(){
	$( "#buttoninteractivity" ).click(function() {
	        $( "#interactivity" ).fadeToggle("slow", "linear");
	});
});

$(function(){
	$( "#buttonelectronics" ).click(function() {
	        $( "#electronics" ).fadeToggle("slow");
	});
});

$(function(){
	$( "#buttonprogramming" ).click(function() {
	        $( "#programming" ).fadeToggle("slow");
	});
}); 

//*resources*//

$(function(){
	$( "#buttonlinks" ).click(function() {
	        $( "#links" ).fadeToggle("slow");
	});
}); 

//****projects****//

$(function(){
	$( "#buttoninspa" ).click(function() {
	        $( "#inspa" ).fadeToggle("slow");
	});
}); 

$(function(){
	$( "#buttonprojects" ).click(function() {
	        $( "#projects" ).fadeToggle("slow");
	});
}); 