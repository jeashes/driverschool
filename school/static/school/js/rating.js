function getStars(rating) {

    // Round to nearest half
    rating = Math.round(rating * 2) / 2;
    let output = [];

    // Append all the filled whole stars
    for (var i = rating; i >= 1; i--)
        output.push('<i class="fa fa-star" aria-hidden="true" style="color: gold;"></i>&nbsp;');

    // If there is a half a star, append it
    if (i == .5) output.push('<i class="fa fa-star-half-o" aria-hidden="true" style="color: gold;"></i>&nbsp;');

    // Fill the empty stars
    for (let i = (5 - rating); i >= 1; i--)
        output.push('<i class="fa fa-star-o" aria-hidden="true" style="color: gold;"></i>&nbsp;');

    return output.join('');

}

function getRating() {
    let ratingWrapper = [...document.getElementsByClassName("school-score")];

    ratingWrapper.map(elementRating =>
        elementRating.getElementsByClassName("stars")[0].innerHTML = getStars(parseInt(elementRating.lastElementChild.textContent))
    )

}

getRating();