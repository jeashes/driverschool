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


function showResultAreaLetter() {
    let areaWrapper = document.getElementsByClassName("area-wrapper"),
        resultWrapper = document.getElementsByClassName("areas-result");

    // let letterWrapper = document.getElementsByClassName("letter-wrapper"),
    //     resultLetter = resultWrapper.textContent.split(" літерою ")[1];


    for (let h=0; h < areaWrapper.length; h++) {
        areaWrapper[h].onclick = function () {
            let result = resultWrapper[0].children[h].textContent.trim()
                    .replaceAll('"', '').split(' ')[2],
                check = areaWrapper[h].textContent.trim();

            if (check == result) {
                for (let k=0; k < resultWrapper[0].children.length; k++) {
                    resultWrapper[0].children[k].classList.remove("test")
                }
                resultWrapper[0].children[h].classList.add("test")
            }
        }
    }

/*
    for (let h=0; h < areaWrapper.length; h++) {
        areaWrapper[h].onclick = function () {
            console.table(resultWrapper[h].children[0].textContent
                        .split(" міста ", 2)[1].trim()
                        .replaceAll('"', '').split(' ')[0])

            console.table(areaWrapper[h].textContent.trim())

            if (resultWrapper[0].children[h].textContent.split(" міста ", 2)[1]
                .trim().replaceAll('"', '').split(' ')[0]
                .includes(areaWrapper[h].textContent.trim())) {

                console.table("yes")
                resultWrapper[h].classList.add("test");

            } else {
                console.table("not")
            }

        }
    }
*/


    // for (let i = 0; i < areaWrapper.length; i++) {
    //
    //     areaWrapper[i].onclick = function () {
    //
    //         console.table(areaWrapper[i]);
    //
    //         if (areaResult[i].includes(areaName[i])) {
    //             areaWrapper[i].classList.add("test");
    //         } else {
    //             areaWrapper[i].classList.remove("test");
    //         }
    //
    //     }
    //
    // }
    //
    // for (let j = 0; j < letterWrapper.length; j++) {
    //
    //     if (letterResult[j].includes(letterName[j])) {
    //         letterName[j].style.display = "flex";
    //     } else {
    //         letterName[j].style.display = "none";
    //     }
    //
    // }

}

showAreaLetter();
showResultAreaLetter();