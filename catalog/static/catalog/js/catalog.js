granel_div = document.getElementsByClassName('Granel');
granel_btn = document.getElementById('granel-btn')
indiv_btn = document.getElementById('indiv-btn')
singles_div = document.getElementsByClassName('Individuais');
filter_div = document.getElementById('filters')
cart = document.getElementById('cart')
detail = document.getElementById('detail')

cart_btn = document.getElementById('cart-btn')

products = document.getElementsByClassName("product-block-1")
products_1 = document.getElementsByClassName("product-block")

function addShowUp() {
	for(i in products) {
		products[i].classList.add('show-up');
	}
}

function addShowUpIndiv() {
	for(i in products_1){
		products_1[i].classList.add('show-up');
	} 
}

function showCart() {
	if(cart.style.display == "none") {
			cart.style.display = "block";
	} else {			
			cart.style.display = "none";
		}
	}


function showDetail() {
	if(detail.style.display == "none") {
			detail.style.display = "block";
	} else {			
			detail.style.display = "none";
		}
	}


function showCartOn() {
	cart.style.display = "block";
}


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
			granel_div[i].style.display = "flex";
			granel_btn.innerHTML = "X"
	} else {
			granel_div[i].style.display = "none";
			granel_btn.innerHTML = "&#9711;"
		}
	}
}

function showSingles(){
	for(i=0; i<singles_div.length; i++) {
		if(singles_div[i].style.display == "none") {
			singles_div[i].style.display = "flex";
			indiv_btn.innerHTML = "X";
		} else {
			singles_div[i].style.display = "none";
			indiv_btn.innerHTML = "&#9711";
		}
	}
}

document.addEventListener('DOMContentLoaded', addShowUp)
document.addEventListener('DOMContentLoaded', addShowUpIndiv)
