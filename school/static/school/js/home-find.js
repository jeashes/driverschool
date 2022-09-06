








function showAreaLetter() {
    let buttonWrapper = document.getElementsByClassName("find-title"),
        areasWrapper = document.getElementsByClassName("areas-block"),
        lettersWrapper = document.getElementsByClassName("letters-block");


    for (let i=0; i < 2; i++) {
        buttonWrapper[i].onclick = function () {
            for (let k=0; k < 2; k++) {
                buttonWrapper[k].classList.remove("active-title");
            }
            buttonWrapper[i].classList.add("active-title");
            if (buttonWrapper[1].classList.contains("active-title")) {
                areasWrapper[0].style.display = "none";
                lettersWrapper[0].style.display = "grid";
            } else {
                lettersWrapper[0].style.display = "none";
                areasWrapper[0].style.display = "grid";
            }
        }
    }
}

function hideShow (result, i) {
    let block =  document.getElementsByClassName("result-block"),
        results = document.getElementsByClassName(result)[0],
        active = document.getElementsByClassName("active-find")[0];


    results.children[i].classList.add("active-find");
    active.classList.add("active-close");

    setTimeout(function() {
        for (let k = 0; k < block.length; k++) {
            block[k].classList.remove("active-find");
            block[k].classList.remove("active-close");
        }
    }, 1000);


}

function showResult(result, wrapper) {
    let results = document.getElementsByClassName(result)[0],
        wrappers = document.getElementsByClassName(wrapper)[0];

        for (let i=0; i < results.children.length; i++) {

        wrappers.children[i].onclick = function () {

            if ($(".active-find").length === 0){
                hideShow(result, i);
            } else {
                hideShow(result, i);
                setTimeout(function() {
                    results.children[i].classList.add("active-find");
                }, 1000);
            }
        }
    }
}

showResult("letters-result", "letters-block");
showResult("areas-result", "areas-block");



showAreaLetter();
