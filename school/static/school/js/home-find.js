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

function showResult(result, wrapper) {
    let Result = document.getElementsByClassName(result)[0],
        Wrapper = document.getElementsByClassName(wrapper)[0],
        Block =  document.getElementsByClassName("result-block");


        for (let i=0; i < Result.children.length; i++) {

        Wrapper.children[i].onclick = function () {
            for (let k = 0; k < Block.length; k++) {
                Block[k].classList.remove("active-find");
            }
                Result.children[i].classList.add("active-find");
        }
    }
}

showResult("letters-result", "letters-block");
showResult("areas-result", "areas-block");



showAreaLetter();
