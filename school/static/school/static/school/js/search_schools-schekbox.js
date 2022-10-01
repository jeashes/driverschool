function submit(evt) {
	evt.preventDefault();
}

function filter(evt) {
	evt.preventDefault();
	let input = document.querySelector('#site-search');
	let inputValue = input.value.toUpperCase();
	let cards = document.querySelectorAll('.item');

	cards.forEach(
		function getMatch(info) {
			let heading = info.querySelector('h3');
			let headingContent = heading.innerHTML.toUpperCase();

			if (headingContent.includes(inputValue)) {
				info.classList.add('show');
				info.classList.remove('hide');
			}
			else {
				info.classList.add('hide');
				info.classList.remove('show');
			}
		}
	)
}

function autoReset() {
	let input = document.querySelector('#site-search');
	let cards = document.querySelectorAll('.item');

	cards.forEach(
		function getMatch(info) {
			if (input.value == null, input.value == "") {
				info.classList.remove('show');
				info.classList.remove('show');
			}
			else {
				return;
			}
		}
	)
}

let form = document.querySelector('.search-form');

form.addEventListener('keyup', filter);

form.addEventListener('submit', submit);