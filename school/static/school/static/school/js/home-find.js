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
        active = document.getElementsByClassName("active-find")[0],
        close = document.getElementsByClassName("active-close")[0];

        if (close) {setTimeout(function() {
        for (let k = 0; k < block.length; k++) {
            block[k].classList.remove("active-find");
            block[k].classList.remove("active-close");
        }
    }, 1000);}

        if (active) {active.classList.add("active-close");}

        if (!active) {results.children[i].classList.add("active-find")}
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
function closeTabs(result) {
    let iconArrow = document.getElementsByClassName("icon-arrow");


    for (let i=0; i < iconArrow.length; i++) {
        iconArrow[i].onclick = function () {
                i > 22
                ? hideShow(result, i-22)
                : hideShow(result, i);

        }
    }


}


showResult("letters-result", "letters-block");
showResult("areas-result", "areas-block");


showAreaLetter();
closeTabs("letters-result");
closeTabs("areas-result");
