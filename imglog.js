//   logs image information (tags listed per image),
//   uses selected tags (prob from some order tbd)
//   (created links on page) to determine which 
//   images to correspondingly display

function pfimg (url, title, date, description, tags) {
	this.url = url;
	this.title = title;
	this.date = date;
	this.description = description;
	this.tags = tags;
	this.writealltest = function(){
		console.log(this.url + " " + this.title + " " + this.date + " " + this.description + " " + this.tags);
	this.tagboolean = false;
	};
};


var tagSearch = function(tagselection){
	numberTags = tagselection.length;
	for (i = 1; i <= tagselection.length; i++) {
		// console.log("Tag #1: " + tagselection[i-1]);
		if (img1.tags.indexOf(tagselection[i-1]) !== -1){
				// console.log(img1.title);
				img1.tagboolean = true;
			};
		if (img2.tags.indexOf(tagselection[i-1]) !== -1){
				// console.log(img2.title);
				img2.tagboolean = true;
			};
		if (img3.tags.indexOf(tagselection[i-1]) !== -1){
				// console.log(img2.title);
				img3.tagboolean = true;
			};	
	};
};

var tagDisplay = function(){
	console.log("DISPLAYING: ");
	if (img1.tagboolean === true){
		console.log(img1.title);
	};
	if (img2.tagboolean === true){
		console.log(img2.title);
	};
	if (img3.tagboolean === true){
		console.log(img3.title);
	};
};

var img1 = new pfimg("/portfolio/selfportrait.jpeg", "Self Portrait", "January 2012", "Portrait juxtaposition art wow k", ["Digital", "Portraiture", "New"]);
var img2 = new pfimg("/portfolio/selfportrait2.jpeg", "Another title", "Some date", "asdjaslkdjalk", ["Digital", "Landscape", "Old"]);
var img3 = new pfimg("/portfolio/selfportrait3.jpeg", "Another title 2", "Some date", "asdjaslkdjalk", ["Digital", "Landscape", "Old"]);


tagSearch(["Landscape"]);
tagDisplay();