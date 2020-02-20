var topblock = document.getElementById('top-block')
var midblock = document.getElementById('middle-block')
var botblock = document.getElementById('bottom-block')
var logo = document.getElementById('logo')
var logo_text = document.getElementById('logo-text')
var logo_2 = document.getElementById('logo-2')
var logo_text_2 = document.getElementById('logo-text-2')
/*
var isInViewport = function(elem) {
	var bounding = elem.getBoundingClientRect();
	return (
		bounding.top >= 0 &&
		bounding.left >= 0 &&
		bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
		bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
	);
}

if(isInViewport(botblock)) {
	botblock.classList.add('show-up')
	console.log('botblock is showing')
}
*/
/*console.log(topblock.getBoundingClientRect())

function popup(el) {
	var bounding = el.getBoundingClientRect();

	if (bounding.top >= 0){
	console.log(el + ' is showing')
	el.classList.add('show-up')
}}

window.addEventListener('scroll', popup(topblock))
window.addEventListener('scroll', popup(midblock))
window.addEventListener('scroll', popup(botblock))
*/
// The checker
const gambitGalleryIsInView = el => {
	const scroll = window.scrollY || window.pageYOffset
	const boundsTop = el.getBoundingClientRect().top + scroll
	
	const viewport = {
		top: scroll,
		bottom: scroll + window.innerHeight,
	}
	
    const bounds = {
		top: boundsTop,
		bottom: boundsTop + el.clientHeight,
	}
	
	return ( bounds.bottom >= viewport.top && bounds.bottom <= viewport.bottom ) 
		|| ( bounds.top <= viewport.bottom && bounds.top >= viewport.top );
}


// Usage.
document.addEventListener( 'DOMContentLoaded', () => {
	const tester = document.querySelector( '.tester' )
	const answer = document.querySelector( '.answer' )
	
	const handler = () => raf( () => {
		logo.classList.add('show-up')
		logo_text.classList.add('show-up')
		logo_2.classList.add('show-up')
		logo_text_2.classList.add('show-up')
	} )
	
	handler()
	window.addEventListener( 'scroll', handler )
} )

// requestAnimationFrame
const raf = 
    window.requestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    function( callback ) {
        window.setTimeout( callback, 1000 / 60 )
    }