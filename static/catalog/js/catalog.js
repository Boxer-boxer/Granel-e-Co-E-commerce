granel_div = document.getElementsByClassName('Granel');
singles_div = document.getElementsByClassName('Individuais');
filter_div = document.getElementById('filters')

function showFilter() {
	if(filter_div.style.display == "none") {
			filter_div.style.display = "flex";
		} else {
			filter_div.style.display = "none";
		}
}



function showGranel(){
	for(i=0; i<granel_div.length; i++) {
		if(granel_div[i].style.display == "none") {
			granel_div[i].style.display = "block";
			filter_div.style.display = "none";
	} else {
			granel_div[i].style.display = "none";
			filter_div.style.display = "none";
		}
	}
}

function showSingles(){
	for(i=0; i<singles_div.length; i++) {
		if(singles_div[i].style.display == "none") {
			singles_div[i].style.display = "block";
			filter_div.style.display = "none";
		} else {
			singles_div[i].style.display = "none";
			filter_div.style.display = "none";
		}
	}
}