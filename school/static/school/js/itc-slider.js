
let slideIndex = 1;

showSlides();


function plusSlides(n) {

  showSlides();

  showSlides( slideIndex += n);

}

function currentSlide(n) {
  showSlides();
}



function showSlides(n) {
  let i;
  let sliderWrapper = document.getElementsByClassName("slideshow-container");

  let dots = document.getElementsByClassName("dot");
  let results = document.getElementsByClassName("areas-block")[0];

    for (let k=0; k < results.children.length; k++) {

      if (n > sliderWrapper[k].children.length) {}
      if (n < 1) {}

      for (i = 0; i < sliderWrapper[k].children.length; i++) {
        sliderWrapper[k].children[i].children[i].style.display = "none";
      }

      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      sliderWrapper[k].children[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";
    }


}


/*

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
>>>>>>> c902e51 (clean code)
  let dots = document.getElementsByClassName("dot");
  let results = document.getElementsByClassName("areas-block")[0];

    for (let k=0; k < results.children.length; k++) {

      if (n > sliderWrapper[k].children.length) {}
      if (n < 1) {}

      for (i = 0; i < sliderWrapper[k].children.length; i++) {
        sliderWrapper[k].children[i].children[i].style.display = "none";
      }

      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      sliderWrapper[k].children[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";
    }


}

=======
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


