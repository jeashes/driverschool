// We have to declare the function for all the sliders

// get all slider from document.
const slideContainer = document.querySelectorAll('.slider');

// lets put your function to every one of them
for(let i = 0; i < slideContainer.length; i++){

    const slider = function (numberSlide) {
        // const this_slider = this;
        const slides = slideContainer[i].querySelectorAll('.slide');  // Your code was : const slides = document.querySelectorAll('.slide');  don't search the entire document, only search the slider
        const btnLeft = slideContainer[i].querySelector('.slider__btn--left');
        const btnRight = slideContainer[i].querySelector('.slider__btn--right');
        const dotContainer = slideContainer[i].querySelector('.dots');


        let curSlide = 0;
        const maxSlide = slides.length;

        // Functions
        const createDots = function () {
                slides.forEach(function (_, i) {
                dotContainer.insertAdjacentHTML(
                'beforeend',
                `<button class="dots__dot" data-slide="${i}"></button>`
                );
            });
        };

        const activateDot = function (slide) {
            slideContainer[i]
                .querySelectorAll('.dots__dot')
                .forEach(dot => dot.classList.remove('dots__dot--active'));

            slideContainer[i]
                .querySelector(`.dots__dot[data-slide="${slide}"]`)
                .classList.add('dots__dot--active');
        };

        const goToSlide = function (slide) {
            slides.forEach(
                (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
            );
        };

        // Next slide
        const nextSlide = function () {
            if (curSlide === maxSlide - 1) {
                curSlide = 0;
            } else {
                curSlide++;
            }
            goToSlide(curSlide);
            activateDot(curSlide);
            culcSliderHeight(curSlide);
        };

        const prevSlide = function () {
            if (curSlide === 0) {
                curSlide = maxSlide - 1;
            } else {
                curSlide--;
            }
            goToSlide(curSlide);
            activateDot(curSlide);
            culcSliderHeight(curSlide);
        };

        const init = function () {
            goToSlide(0);
            createDots();

            activateDot(0);
        };
        init();

        // Event handlers
        btnRight.addEventListener('click', nextSlide);
        btnLeft.addEventListener('click', prevSlide);

        document.addEventListener('keydown', function (e) {
            if (e.key === 'ArrowLeft') prevSlide();
            e.key === 'ArrowRight' && nextSlide();
        });

        dotContainer.addEventListener('click', function (e) {
            if (e.target.classList.contains('dots__dot')) {
                const { slide } = e.target.dataset;
                goToSlide(slide);
                activateDot(slide);
                culcSliderHeight();
            }
        });
        const culcSliderHeight = (curSlide) => {
            if (slideContainer[0].parentNode.classList.contains("result-wrapper")) {
                console.log(slides[curSlide].clientHeight)
                const sliderHeight = slides[curSlide].clientHeight;
                slideContainer[i].style.height = `${sliderHeight}px`;
            } else {
                btnLeft.style.bottom = "60px"
                btnRight.style.bottom = "60px"
            }

        }
        culcSliderHeight(curSlide);
    };
    slider();
}
